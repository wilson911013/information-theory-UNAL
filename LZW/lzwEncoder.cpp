#include<bits/stdc++.h>
#include<stdint.h>
#include<assert.h>

using namespace std;

class Encoder{
    uint16_t max_code;
public:
    Encoder(uint16_t _max_code){
        max_code = _max_code;
    }

    Encoder() : Encoder(4095) {}

    vector<uint16_t> encode(string file_name){
        FILE * file;

        map<vector<uint8_t>, uint16_t> dict;
        for(int i = 0 ; i <= 255 ; i++){
            vector<uint8_t> word;
            word.push_back(i);
            dict[word] = i;
        }

        uint8_t buffer[1];
        file = fopen(file_name.c_str(), "rb");
        if(!file){
            cerr << "Error opening the file" << endl;
        }
        //////////////////////////////////////////////////

        vector<uint8_t> word;
        vector<uint16_t> result;
        vector<uint8_t> word_c;

        while(fread(buffer, sizeof(buffer), 1, file) > 0){
            assert(dict.size() <= max_code);

            word_c = word;
            word_c.push_back(buffer[0]);

            auto it = dict.find(word_c);
            if(it != dict.end()){
                word = word_c;
            }else{
                result.push_back(dict[word]);
                int dict_size = dict.size();
                if(dict_size < max_code){
                    dict[word_c] = dict_size;
                }
                vector<uint8_t> aux;
                aux.push_back(buffer[0]);
                word = aux;
            }
        } 

        if(word.size() > 0){
            result.push_back(dict[word]);
        }

        if( fclose(file) != 0 ){
            cerr << "Error closing the file" << endl;
        }

        return result;
    }

    void wirte_encoded(string src, string file_name){
        FILE * file;

        file = fopen(file_name.c_str(), "wb");
        if(!file){
            cerr << "Error opening the file" << endl;
        }

        auto compressed = encode(src);

        // int mx = 0;
        // for(auto i : compressed) mx = max(mx, (int)i);
        // cerr<<mx<<endl;

        uint8_t additional = compressed.size() & 0x01;

        if(additional != 0){
            compressed.push_back(0);
        }

        fwrite(&additional, sizeof(additional), 1, file);

        uint8_t chunk[3];
        for(int i = 0 ; i < compressed.size() ; i+=2){
            chunk[0] = (compressed[i] & 0x00FF);
            chunk[1] = ( ( (compressed[i] & 0x0F00) >> 8 ) | ( (compressed[i + 1] & 0x000F) << 4 ) );
            chunk[2] = ( (compressed[i + 1] & 0x0FF0) >> 4 );
            fwrite(chunk, sizeof(chunk), 1, file);
        }

        if( fclose(file) != 0 ){
            cerr << "Error closing the file" << endl;
        }
    }

    void write_decode(string original, string compressed){
        FILE * cFile;
        cFile = fopen(compressed.c_str(), "rb");
        if(!cFile){
            cerr << "Error opening the file" << endl;
        }

        uint8_t additional;
        fread(&additional, sizeof(additional), 1, cFile);

        vector<uint16_t> comp;
        uint8_t chunk[3];
        while(fread(chunk, sizeof(chunk), 1, cFile) > 0){
            uint16_t a1 = chunk[0];
            a1 |= ( (chunk[1] & 0x0F) << 8 ) ;
            uint16_t a2 = ( (chunk[1] & 0xF0) >> 4 );
            a2 |= (chunk[2] << 4);
            comp.push_back(a1);
            comp.push_back(a2);
        }

        if( additional == 1 ){
            comp.pop_back();
        }

        if( fclose(cFile) != 0){
            cerr << "Error closing the file" << endl;
        }

        FILE * oFile;
        oFile = fopen(original.c_str(), "wb");

        auto des = decode(comp);
        for(auto c: des){
            fwrite(&c, sizeof(c), 1, oFile);
        }
        if( fclose(oFile) != 0){
            cerr << "Error closing the file" << endl;
        }
    }

    vector<uint8_t> decode(vector<uint16_t> compressed){
        map< uint16_t, vector<uint8_t> > dict;
        for(int i = 0 ; i <= 255 ; i++){
            vector<uint8_t> word;
            word.push_back(i);
            dict[i] = word;
        }


        vector<uint8_t> result;

        vector<uint8_t> word;
        word.push_back(compressed[0]);
        result.push_back(compressed[0]);

        for(int i = 1 ; i < compressed.size() ; i++){
            assert( dict.size() <= max_code );
            uint16_t k = compressed[i];

            auto it = dict.find(k);
            vector<uint8_t> entry;

            if(it != dict.end()){
                entry = dict[k];
            }else if (k == dict.size()){
                entry = word;
                entry.push_back(word[0]); 
            }else{
                cerr<<"Bad compressed"<<endl;
            }
            for(auto u: entry){
                result.push_back(u);
            }

            auto aux = word;
            aux.push_back(entry[0]);

            if (dict.size() < max_code) {
                dict[dict.size()] = aux;
            }
            word = entry;
        }

        return result;
    }
};

class Test{
public:
    Test(){};
    virtual void run(){};

    bool compare_files(const std::string &filename1, const std::string &filename2){
        std::ifstream file1(filename1, std::ifstream::ate | std::ifstream::binary); //open file at the end
        std::ifstream file2(filename2, std::ifstream::ate | std::ifstream::binary); //open file at the end
        const std::ifstream::pos_type fileSize = file1.tellg();

        if (fileSize != file2.tellg())
        {
            return false; //different file size
        }

        file1.seekg(0); //rewind
        file2.seekg(0); //rewind

        std::istreambuf_iterator<char> begin1(file1);
        std::istreambuf_iterator<char> begin2(file2);

        return std::equal(begin1, std::istreambuf_iterator<char>(), begin2); //Second argument is end-of-range iterator
    }
};

class TestEncoder: Test{
public:
    TestEncoder(){};
    void run(string file_to_compress){
        string name_no_extension = file_to_compress.substr(0, file_to_compress.find("."));
        string extension = file_to_compress.substr( file_to_compress.find(".") );
        
        string compressed_file_name = name_no_extension + "_compressed.mauro";
        string decompressed_file_name = name_no_extension + "_decompressed" + extension;

        Encoder encoder;
        encoder.wirte_encoded(file_to_compress, compressed_file_name);
        encoder.write_decode(decompressed_file_name, compressed_file_name);

        assert(compare_files(file_to_compress, decompressed_file_name));
    }
};

vector<string> files;

void test_algorithm(){
    TestEncoder test;
    for(auto file_name : files){
        cout<<"Testing " << file_name << "..." << endl;
        test.run(file_name);
    }
}

int main(){
    files.push_back("test_files/text/example1.txt");
    files.push_back("test_files/text/rfc2616.txt");
    files.push_back("test_files/text/bible.txt");
    files.push_back("test_files/wav/about_a_girl.wav");
    files.push_back("test_files/wav/wind_of_change.wav");
    files.push_back("test_files/wav/every_breath_you_take.wav");
    files.push_back("test_files/wav/d.wav");

    test_algorithm();
}
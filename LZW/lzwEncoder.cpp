#include<bits/stdc++.h>
#include<stdint.h>
using namespace std;

const uint16_t max_code = 4095;

class Encoder{
public:
    Encoder(){
    }

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
                
            word_c = word;
            word_c.push_back(buffer[0]);
            //printf("Readed: %c ", buffer[0]);
            //printf("%c", buffer[0]);

            auto it = dict.find(word_c);
            if(it != dict.end()){
                word = word_c;
            }else{
                //printf("&%x\n", dict[word]);
                //if(dict.size() == 256 || true){
                //    printf("%x: ", dict.size());
                //    for(auto u: word_c) printf("%c", u);
                //}
                //printf(" _ ");
                //for(auto u: word) printf("%c", u);
                //printf(" _ %x \n", dict[word]);
                result.push_back(dict[word]);
                int dict_size = dict.size();
                if(dict_size <= max_code){
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

        // printf("\n");
        // for(auto i : result){
        //     printf("%x ", i);
        // }

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

        int mx = 0;
        for(auto i : compressed) mx = max(mx, (int)i);
        cerr<<mx<<endl;

        while(compressed.size() % 2 != 0){
            compressed.push_back(0);
        }

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
            uint16_t k = compressed[i];

            auto it = dict.find(k);
            vector<uint8_t> entry;

            if(it != dict.end()){
                entry = dict[k];
                // if(k == 257){
                //     for(auto u: entry){
                //         printf("%c", u);
                //     }printf("\n");
                // } 
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
            dict[dict.size()] = aux;
            word = entry;
        }

        // for(auto u: result){
        //     printf("%c", u);
        // }printf("\n");

        return result;
    }
};


int main(){
    uint8_t buffer[1];
    //string file_name = "test.txt";
    //FILE * file;
    //file = fopen(file_name.c_str(), "rb");
    
    Encoder e;
    // auto compressed = e.encode("test.txt");
    // printf("\n");   
    // e.decode(compressed);
    
    
    e.wirte_encoded("test.txt", "compressed.mcf");
    e.write_decode("worked.txt", "compressed.mcf");
}
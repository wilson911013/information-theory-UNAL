clc
clear

//Inputs
    frecuency = 1;
    frecuency_multiplier = 10;
//End of inputs

//Plot analog function
    plot_divisions = 200;
    period = 1 / frecuency;
    
    min_analog_t = 0;
    max_analog_t = 2 * period;
    
    analog_t = linspace(min_analog_t, max_analog_t, plot_divisions);
    analog_y = cos(2 * %pi * frecuency * analog_t);
    //subplot(221);
    plot(analog_t, analog_y);
//End plot of analog function

//Plot of discrete function
    frecuency_of_sample = frecuency_multiplier * frecuency;
    period_of_sample = 1 / frecuency_of_sample;
    discrete_frecuency = frecuency / frecuency_of_sample;
    
    min_discrete_t = ceil(min_analog_t / period_of_sample);
    max_discrete_t = floor(max_analog_t / period_of_sample);
    
    discrete_t = min_discrete_t:max_discrete_t;
    discrete_y = cos(2 * %pi * discrete_frecuency * discrete_t);
    //subplot(221);
    plot(period_of_sample * discrete_t, discrete_y, '*r');
//End of plot of discrete function

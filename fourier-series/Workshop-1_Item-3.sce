function z = original_f(x)
    if x < 0 then
        disp(x)
        z = 0
    else
        z = %pi - x
    end
endfunction

function z = f(x)
    z = 0
endfunction

x = [-1*%pi : 0.01 : %pi]
y = f(x)
plot(x,y)

function [text] = calculator_FUC(x,n)
% calculator_FUC - 三角函数计算器
%
% 输入参数：
%   x - 输入变量，可以是一个角度，也可以是一个数值
%   n - 输入变量，为1计算sin函数,为2计算cos函数,为3计算arctan函数，为4计算arcsin函数
%
% 输出显示：
%   text - 计算得到的三角函数值


%sin函数获取，输入为角度，输出为数值
sin_taylor_module = py.importlib.import_module('sin_taylor');
sin_taylor_func = sin_taylor_module.sin_taylor;

%cos函数获取,输入为角度，输出为数值
cos_taylor_module = py.importlib.import_module('cos_taylor');
cos_taylor_func = cos_taylor_module.cos_taylor;

%arctan函数获取，输入为数值，输出为角度
arctan_newton_module = py.importlib.import_module('arctan_newton');
arctan_newton_func = arctan_newton_module.arctan_newton;

%arcsin函数获取，输入为数值，输出为角度
arcsin_taylor_module = py.importlib.import_module('arcsin_taylor');
arcsin_taylor_func = arcsin_taylor_module.arcsin_taylor;



switch n
    case 'sin'
        y_sin=sin_taylor_func(x);
        text =['sin(', num2str(x), '°) = ', num2str(y_sin)];
    case 'cos'
        y_cos=cos_taylor_func(x);
        text =['cos(', num2str(x), '°) = ', num2str(y_cos)];
    case 'arctan'
        y_arctan=double(arctan_newton_func(x));
        text=['arctan(', num2str(x), ') = ', num2str(y_arctan),'°'];
    case 'arcsin'
        y_arcsin=arcsin_taylor_func(x);
        text=['arcsin(', num2str(x), ') = ', num2str(y_arcsin),'°'];
end
end



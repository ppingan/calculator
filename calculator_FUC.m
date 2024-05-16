function [text] = calculator_FUC(x,n)
% calculator_FUC - ���Ǻ���������
%
% ���������
%   x - ���������������һ���Ƕȣ�Ҳ������һ����ֵ
%   n - ���������Ϊ1����sin����,Ϊ2����cos����,Ϊ3����arctan������Ϊ4����arcsin����
%
% �����ʾ��
%   text - ����õ������Ǻ���ֵ


%sin������ȡ������Ϊ�Ƕȣ����Ϊ��ֵ
sin_taylor_module = py.importlib.import_module('sin_taylor');
sin_taylor_func = sin_taylor_module.sin_taylor;

%cos������ȡ,����Ϊ�Ƕȣ����Ϊ��ֵ
cos_taylor_module = py.importlib.import_module('cos_taylor');
cos_taylor_func = cos_taylor_module.cos_taylor;

%arctan������ȡ������Ϊ��ֵ�����Ϊ�Ƕ�
arctan_newton_module = py.importlib.import_module('arctan_newton');
arctan_newton_func = arctan_newton_module.arctan_newton;

%arcsin������ȡ������Ϊ��ֵ�����Ϊ�Ƕ�
arcsin_taylor_module = py.importlib.import_module('arcsin_taylor');
arcsin_taylor_func = arcsin_taylor_module.arcsin_taylor;



switch n
    case 'sin'
        y_sin=sin_taylor_func(x);
        text =['sin(', num2str(x), '��) = ', num2str(y_sin)];
    case 'cos'
        y_cos=cos_taylor_func(x);
        text =['cos(', num2str(x), '��) = ', num2str(y_cos)];
    case 'arctan'
        y_arctan=double(arctan_newton_func(x));
        text=['arctan(', num2str(x), ') = ', num2str(y_arctan),'��'];
    case 'arcsin'
        y_arcsin=arcsin_taylor_func(x);
        text=['arcsin(', num2str(x), ') = ', num2str(y_arcsin),'��'];
end
end



classdef App2 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        Cal                   matlab.ui.Figure                   % ���Ǻ���������
        LabelNumericEditField matlab.ui.control.Label            % �����
        Input                 matlab.ui.control.NumericEditField % [-Inf Inf]
        Label                 matlab.ui.control.Label            % ���Ǻ���������
        Readme                matlab.ui.control.TextArea         % ʹ��˵����
        ButtonGroup           matlab.ui.container.ButtonGroup    % ����ѡ��
        RadioButton           matlab.ui.control.RadioButton      % sin
        RadioButton2          matlab.ui.control.RadioButton      % cos
        RadioButton3          matlab.ui.control.RadioButton      % arcsin
        RadioButton4          matlab.ui.control.RadioButton      % arctan
        LabelEditField        matlab.ui.control.Label            % sin ��
        Output                matlab.ui.control.EditField       
        Button                matlab.ui.control.Button           % ����
    end


    properties (Access = public)
        mode % ���㹦��ѡ�� 1.sin 2.cos 3.arctan 4.arcsin
    end

    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            app.mode = 'sin'; %Ĭ�ϼ��㹦��
        end

        % ButtonGroup selection change function
        function ButtonGroupSelectionChanged(app, event)
            selectedButton = app.ButtonGroup.SelectedObject;
            app.mode = selectedButton.Text;
            switch app.mode
                case'sin'   %���Ϊsina
                    app.LabelEditField.Text = 'sin ��'; 
                case'cos'   %���Ϊcosa
                    app.LabelEditField.Text = 'cos ��';       
                case'arctan'   %���Ϊarctana
                    app.LabelEditField.Text = 'arctan ��';   
                case'arcsin'  %���Ϊarcsina
                    app.LabelEditField.Text = 'arcsin ��';   
            end 
        end

        % Button button pushed function
        function ButtonButtonPushed(app)
            %����ֵ
            x = app.Input.Value;
            %�������Ǻ���ֵ�����
             [app.Output.Value]=calculator_FUC(x,app.mode);     
        end
    end

    % App initialization and construction
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create Cal
            app.Cal = uifigure;
            app.Cal.Position = [100 100 511 478];
            app.Cal.Name = '���Ǻ���������';
            setAutoResize(app, app.Cal, false)

            % Create LabelNumericEditField
            app.LabelNumericEditField = uilabel(app.Cal);
            app.LabelNumericEditField.BackgroundColor = [0.9373 0.9373 0.9373];
            app.LabelNumericEditField.HorizontalAlignment = 'center';
            app.LabelNumericEditField.VerticalAlignment = 'center';
            app.LabelNumericEditField.FontSize = 16;
            app.LabelNumericEditField.FontWeight = 'bold';
            app.LabelNumericEditField.Position = [265 148 43 20];
            app.LabelNumericEditField.Text = '�����';

            % Create Input
            app.Input = uieditfield(app.Cal, 'numeric');
            app.Input.FontSize = 16;
            app.Input.Position = [326 148 62 20];

            % Create Label
            app.Label = uilabel(app.Cal);
            app.Label.BackgroundColor = [0.9255 0.6941 0.102];
            app.Label.HorizontalAlignment = 'center';
            app.Label.VerticalAlignment = 'center';
            app.Label.FontName = '����';
            app.Label.FontSize = 24;
            app.Label.FontWeight = 'bold';
            app.Label.Position = [209 486 233 59];
            app.Label.Text = '���Ǻ���������';

            % Create Readme
            app.Readme = uitextarea(app.Cal);
            app.Readme.FontSize = 14;
            app.Readme.FontColor = [1 0 0];
            app.Readme.Position = [129 338 394 116];
            app.Readme.Value = {'ʹ��˵����'; '���ڡ�����ѡ����ѡ��sin������cos������arctan����arcsin�������ڡ�������������������Ķ�������������㡱��ť�����ɵõ���Ӧ�ļ�������������sin��cos����ֱ������Ƕȣ�����arcsin��arctan����ֱ��������ֵ��'};

            % Create ButtonGroup
            app.ButtonGroup = uibuttongroup(app.Cal);
            app.ButtonGroup.SelectionChangedFcn = createCallbackFcn(app, @ButtonGroupSelectionChanged, true);
            app.ButtonGroup.BorderType = 'line';
            app.ButtonGroup.TitlePosition = 'centertop';
            app.ButtonGroup.Title = '����ѡ��';
            app.ButtonGroup.FontName = 'Helvetica';
            app.ButtonGroup.FontWeight = 'bold';
            app.ButtonGroup.FontUnits = 'pixels';
            app.ButtonGroup.FontSize = 16;
            app.ButtonGroup.Units = 'pixels';
            app.ButtonGroup.Position = [275 196 103 123];

            % Create RadioButton
            app.RadioButton = uiradiobutton(app.ButtonGroup);
            app.RadioButton.Text = 'sin';
            app.RadioButton.Position = [10 71 35 16];
            app.RadioButton.Value = true;

            % Create RadioButton2
            app.RadioButton2 = uiradiobutton(app.ButtonGroup);
            app.RadioButton2.Text = 'cos';
            app.RadioButton2.Position = [10 49 38 16];

            % Create RadioButton3
            app.RadioButton3 = uiradiobutton(app.ButtonGroup);
            app.RadioButton3.Text = 'arctan';
            app.RadioButton3.Position = [10 26 52 16];

            % Create RadioButton4
            app.RadioButton4 = uiradiobutton(app.ButtonGroup);
            app.RadioButton4.Text = 'arcsin';
            app.RadioButton4.Position = [10 4 53 16];

            % Create LabelEditField
            app.LabelEditField = uilabel(app.Cal);
            app.LabelEditField.HorizontalAlignment = 'right';
            app.LabelEditField.FontSize = 16;
            app.LabelEditField.FontWeight = 'bold';
            app.LabelEditField.Position = [135 48 70 20];
            app.LabelEditField.Text = 'sin ��';

            % Create Output
            app.Output = uieditfield(app.Cal, 'text');
            app.Output.HorizontalAlignment = 'center';
            app.Output.FontSize = 16;
            app.Output.FontWeight = 'bold';
            app.Output.Position = [216 44 221 28];

            % Create Button
            app.Button = uibutton(app.Cal, 'push');
            app.Button.ButtonPushedFcn = createCallbackFcn(app, @ButtonButtonPushed);
            app.Button.BackgroundColor = [0.902 0.2235 0.2235];
            app.Button.FontName = '����';
            app.Button.FontSize = 16;
            app.Button.FontWeight = 'bold';
            app.Button.Position = [268 96 118 34];
            app.Button.Text = '����';
        end
    end

    methods (Access = public)

        % Construct app
        function app = App2()

            % Create and configure components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.Cal)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.Cal)
        end
    end
end
%-------------------------------------------------------------------------%
%                         Hewlett-Packard Company
%                        Summer Internship  - 2015
%                           Tiago Rosa dos Reis 
%              Engineering Modeling & Analysis Group (EMAG)
%                   Drop Head Velocity Comparison Tool
%-------------------------------------------------------------------------%
close all
clear variables
clc
%-------------------------------------------------------------------------%
input('Press ENTER to start');
fprintf('\n')
fprintf('\n')
%-------------------------------------------------------------------------%

% This post-processing tool was developed to identify potential gaps
% between experimental data (including BLD and high-speed camera ReTINA)
% and the computational model provided by CFD3.

% This MATLAB script identifies the time when the droplet leaves the bore 
% based on the experimental data from the ReTINA datasheet and 
% automatically plots multiple curves for different CFD3 simulations in a 
% comparison with ReTINA and BLD. 

% It also calculates the surface tension for every curve based on the peak 
% values of oscillation. The accuracy of the results for surface tension 
% needs improvement. In some cases it is difficult to identify the peaks of
% oscillation (i.e. multiple squares appear on the plot) or the drop weight
% values used to obtain the drop radius are inaccurate. PRESS F5 TO RUN.

%=========================================================================%

%-------------------------------------------------------------------------%
% DATA SETUP
%-------------------------------------------------------------------------%

%=========================================================================%

%-------------------------------------------------------------------------%
% RETINA-X FILES
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
A = xlsread('3452_F1_DHV.xlsx'); % F1 Retina
B = xlsread('3452_C1_DHV.xlsx'); % C1 Retina
C = xlsread('3452_AA2_DHV.xlsx'); % Puffer Retina
D = xlsread('3452_NemK_DHV.xlsx'); % Nemesis Retina

R = cell(1,4); % MATRIX FOR ALL RETINA DATA
R{1,1} = A; R{1,2} = B; R{1,3} = C; R{1,4} = D;
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
% BLD FILES
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
BLD1 = xlsread('BLD_3452_F1_DV.xlsx'); % F1 SURFACTANT
BLD2 = xlsread('BLD_3452_C1_DV.xlsx'); % C1 SURFACTANT
BLD3 = xlsread('BLD_3452_PufferK_DV.xlsx'); % PUFFER-K
BLD4 = zeros(size(BLD1)); % NemK = 0 -> Introduce values 

BLD = cell(1,4);
BLD{1,1} = BLD1; BLD{1,2} = BLD2; BLD{1,3} = BLD3; BLD{1,4} = BLD4;
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
% CFD3 FILES
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%

V_crit = [0.25 0.50 0.75 1.0]; % Not necessary so far

for vcrit=1:length(V_crit)
    
    if vcrit == 1 % Vcrit = 0.25
        
        %---------------%
        % F1 SURFACTANT
        %---------------%
        
        A1 = xlsread('f1dye_55_0.8_20_1e5_0.25.xlsx'); % 1e5 (P_floor)
        A2 = xlsread('f1dye_55_0.8_40_1e5_0.25.xlsx'); % 1e5 (P_floor)
        A3 = xlsread('f1dye_55_0.8_70_1e5_0.25.xlsx'); % 1e5 (P_floor)
        A4 = xlsread('f1dye_55_0.8_20_5e5_0.25.xlsx'); % 5e5 (P_floor)
        A5 = xlsread('f1dye_55_0.8_40_5e5_0.25.xlsx'); % 5e5 (P_floor)
        A6 = xlsread('f1dye_55_0.8_70_5e5_0.25.xlsx'); % 5e5 (P_floor)
        
        %---------------%
        % C1 SURFACTANT
        %---------------%
        
        B1 = xlsread('C1_20_1e5_0.25.xlsx'); % 1e5 (P_floor)
        B2 = xlsread('C1_40_1e5_0.25.xlsx'); % 1e5 (P_floor)
        B3 = xlsread('C1_70_1e5_0.25.xlsx'); % 1e5 (P_floor)
        B4 = xlsread('C1_20_5e5_0.25.xlsx'); % 5e5 (P_floor)
        B5 = xlsread('C1_40_5e5_0.25.xlsx'); % 5e5 (P_floor)
        B6 = xlsread('C1_70_5e5_0.25.xlsx'); % 5e5 (P_floor)
        
        %-------------%
        % PUFFER K
        %-------------%
        
        C1 = xlsread('pufk_55_1.0_20_1e5_0.25.xlsx'); % 1e5 (P_floor)
        C2 = xlsread('pufk_55_1.0_40_1e5_0.25.xlsx'); % 1e5 (P_floor)
        C3 = xlsread('pufk_55_1.0_70_1e5_0.25.xlsx'); % 1e5 (P_floor)
        C4 = xlsread('pufk_55_1.0_20_5e5_0.25.xlsx'); % 5e5 (P_floor)
        C5 = xlsread('pufk_55_1.0_40_5e5_0.25.xlsx'); % 5e5 (P_floor)
        C6 = xlsread('pufk_55_1.0_70_5e5_0.25.xlsx'); % 5e5 (P_floor)
        
        %-----------%
        % NEMESIS K
        %-----------%
        
        D1 = xlsread('NemK_20_1e5_0.25.xlsx'); % 1e5 (P_floor)
        D2 = xlsread('NemK_40_1e5_0.25.xlsx'); % 1e5 (P_floor)
        D3 = xlsread('NemK_70_1e5_0.25.xlsx'); % 1e5 (P_floor)
        D4 = xlsread('NemK_20_5e5_0.25.xlsx'); % 5e5 (P_floor)
        D5 = xlsread('NemK_40_5e5_0.25.xlsx'); % 5e5 (P_floor)
        D6 = xlsread('NemK_70_5e5_0.25.xlsx'); % 5e5 (P_floor)
        
    end
    
    if vcrit == 2 % Vcrit = 0.50
        
        %---------------%
        % F1 SURFACTANT
        %---------------%
        
        A1 = xlsread('f1dye_55_0.8_20_1e5_0.50.xlsx'); % 1e5 (P_floor)
        A2 = xlsread('f1dye_55_0.8_40_1e5_0.50.xlsx'); % 1e5 (P_floor)
        A3 = xlsread('f1dye_55_0.8_70_1e5_0.50.xlsx'); % 1e5 (P_floor)
        A4 = xlsread('f1dye_55_0.8_20_5e5_0.50.xlsx'); % 5e5 (P_floor)
        A5 = xlsread('f1dye_55_0.8_40_5e5_0.50.xlsx'); % 5e5 (P_floor)
        A6 = xlsread('f1dye_55_0.8_70_5e5_0.50.xlsx'); % 5e5 (P_floor)
        
        %---------------%
        % C1 SURFACTANT
        %---------------%
        
        B1 = xlsread('C1_20_1e5_0.50.xlsx'); % 1e5 (P_floor)
        B2 = xlsread('C1_40_1e5_0.50.xlsx'); % 1e5 (P_floor)
        B3 = xlsread('C1_70_1e5_0.50.xlsx'); % 1e5 (P_floor)
        B4 = xlsread('C1_20_5e5_0.50.xlsx'); % 5e5 (P_floor)
        B5 = xlsread('C1_40_5e5_0.50.xlsx'); % 5e5 (P_floor)
        B6 = xlsread('C1_70_5e5_0.50.xlsx'); % 5e5 (P_floor)
        
        %-------------%
        % PUFFER K
        %-------------%
        
        C1 = xlsread('pufk_55_1.0_20_1e5_0.50.xlsx'); % 1e5 (P_floor)
        C2 = xlsread('pufk_55_1.0_40_1e5_0.50.xlsx'); % 1e5 (P_floor)
        C3 = xlsread('pufk_55_1.0_70_1e5_0.50.xlsx'); % 1e5 (P_floor)
        C4 = xlsread('pufk_55_1.0_20_5e5_0.50.xlsx'); % 5e5 (P_floor)
        C5 = xlsread('pufk_55_1.0_40_5e5_0.50.xlsx'); % 5e5 (P_floor)
        C6 = xlsread('pufk_55_1.0_70_5e5_0.50.xlsx'); % 5e5 (P_floor)
        
        %-----------%
        % NEMESIS K
        %-----------%
        
        D1 = xlsread('NemK_20_1e5_0.50.xlsx'); % 1e5 (P_floor)
        D2 = xlsread('NemK_40_1e5_0.50.xlsx'); % 1e5 (P_floor)
        D3 = xlsread('NemK_70_1e5_0.50.xlsx'); % 1e5 (P_floor)
        D4 = xlsread('NemK_20_5e5_0.50.xlsx'); % 5e5 (P_floor)
        D5 = xlsread('NemK_40_5e5_0.50.xlsx'); % 5e5 (P_floor)
        D6 = xlsread('NemK_70_5e5_0.50.xlsx'); % 5e5 (P_floor)
        
    end
    
    if vcrit == 3 % Vcrit = 0.75
        
        %---------------%
        % F1 SURFACTANT
        %---------------%
        
        A1 = xlsread('f1dye_55_0.8_20_1e5_0.75.xlsx'); % 1e5 (P_floor)
        A2 = xlsread('f1dye_55_0.8_40_1e5_0.75.xlsx'); % 1e5 (P_floor)
        A3 = xlsread('f1dye_55_0.8_70_1e5_0.75.xlsx'); % 1e5 (P_floor)
        A4 = xlsread('f1dye_55_0.8_20_5e5_0.75.xlsx'); % 5e5 (P_floor)
        A5 = xlsread('f1dye_55_0.8_40_5e5_0.75.xlsx'); % 5e5 (P_floor)
        A6 = xlsread('f1dye_55_0.8_70_5e5_0.75.xlsx'); % 5e5 (P_floor)
        
        %---------------%
        % C1 SURFACTANT
        %---------------%
        
        B1 = xlsread('C1_20_1e5_0.75.xlsx'); % 1e5 (P_floor)
        B2 = xlsread('C1_40_1e5_0.75.xlsx'); % 1e5 (P_floor)
        B3 = xlsread('C1_70_1e5_0.75.xlsx'); % 1e5 (P_floor)
        B4 = xlsread('C1_20_5e5_0.75.xlsx'); % 5e5 (P_floor)
        B5 = xlsread('C1_40_5e5_0.75.xlsx'); % 5e5 (P_floor)
        B6 = xlsread('C1_70_5e5_0.75.xlsx'); % 5e5 (P_floor)
        
        %-------------%
        % PUFFER K
        %-------------%
        
        C1 = xlsread('pufk_55_1.0_20_1e5_0.75.xlsx'); % 1e5 (P_floor)
        C2 = xlsread('pufk_55_1.0_40_1e5_0.75.xlsx'); % 1e5 (P_floor)
        C3 = xlsread('pufk_55_1.0_70_1e5_0.75.xlsx'); % 1e5 (P_floor)
        C4 = xlsread('pufk_55_1.0_20_5e5_0.75.xlsx'); % 5e5 (P_floor)
        C5 = xlsread('pufk_55_1.0_40_5e5_0.75.xlsx'); % 5e5 (P_floor)
        C6 = xlsread('pufk_55_1.0_70_5e5_0.75.xlsx'); % 5e5 (P_floor)
        
        %-----------%
        % NEMESIS K
        %-----------%
        
        D1 = xlsread('NemK_20_1e5_0.75.xlsx'); % 1e5 (P_floor)
        D2 = xlsread('NemK_40_1e5_0.75.xlsx'); % 1e5 (P_floor)
        D3 = xlsread('Nemk_70_1e5_0.75.xlsx'); % 1e5 (P_floor)
        D4 = xlsread('NemK_20_5e5_0.75.xlsx'); % 5e5 (P_floor)
        D5 = xlsread('NemK_40_5e5_0.75.xlsx'); % 5e5 (P_floor)
        D6 = xlsread('NemK_70_5e5_0.75.xlsx'); % 5e5 (P_floor)
        
    end
    
    if vcrit == 4 % Vcrit = 1.00
        
        %---------------%
        % F1 SURFACTANT
        %---------------%
        
        A1 = xlsread('f1dye_55_0.8_20_1e5_1.00.xlsx'); % 1e5 (P_floor)
        A2 = xlsread('f1dye_55_0.8_40_1e5_1.00.xlsx'); % 1e5 (P_floor)
        A3 = xlsread('f1dye_55_0.8_70_1e5_1.00.xlsx'); % 1e5 (P_floor)
        A4 = xlsread('f1dye_55_0.8_20_5e5_1.00.xlsx'); % 5e5 (P_floor)
        A5 = xlsread('f1dye_55_0.8_40_5e5_1.00.xlsx'); % 5e5 (P_floor)
        A6 = xlsread('f1dye_55_0.8_70_5e5_1.00.xlsx'); % 5e5 (P_floor)
                
        %---------------%
        % C1 SURFACTANT
        %---------------%
        
        B1 = xlsread('C1_20_1e5_1.00.xlsx'); % 1e5 (P_floor)
        B2 = xlsread('C1_40_1e5_1.00.xlsx'); % 1e5 (P_floor)
        B3 = xlsread('C1_70_1e5_1.00.xlsx'); % 1e5 (P_floor)
        B4 = xlsread('C1_20_5e5_1.00.xlsx'); % 5e5 (P_floor)
        B5 = xlsread('C1_40_5e5_1.00.xlsx'); % 5e5 (P_floor)
        B6 = xlsread('C1_70_5e5_1.00.xlsx'); % 5e5 (P_floor)
        
        %-------------%
        % PUFFER K
        %-------------%
        
        C1 = xlsread('pufk_55_1.0_20_1e5_1.00.xlsx'); % 1e5 (P_floor)
        C2 = xlsread('pufk_55_1.0_40_1e5_1.00.xlsx'); % 1e5 (P_floor)
        C3 = xlsread('pufk_55_1.0_70_1e5_1.00.xlsx'); % 1e5 (P_floor)
        C4 = xlsread('pufk_55_1.0_20_5e5_1.00.xlsx'); % 5e5 (P_floor)
        C5 = xlsread('pufk_55_1.0_40_5e5_1.00.xlsx'); % 5e5 (P_floor)
        C6 = xlsread('pufk_55_1.0_70_5e5_1.00.xlsx'); % 5e5 (P_floor)
        
        %-----------%
        % NEMESIS K
        %-----------%
        
        D1 = xlsread('NemK_20_1e5_1.00.xlsx'); % 1e5 (P_floor)
        D2 = xlsread('NemK_40_1e5_1.00.xlsx'); % 1e5 (P_floor)
        D3 = xlsread('NemK_70_1e5_1.00.xlsx'); % 1e5 (P_floor)
        D4 = xlsread('NemK_20_5e5_1.00.xlsx'); % 5e5 (P_floor)
        D5 = xlsread('NemK_40_5e5_1.00.xlsx'); % 5e5 (P_floor)
        D6 = xlsread('NemK_70_5e5_1.00.xlsx'); % 5e5 (P_floor)
        
    end
  
    % Assembly Matrix
    %-----------------%
    H1 = [A1 A2 A3 A4 A5 A6]; % HISTORY FILE
    H2 = [B1 B2 B3 B4 B5 B6]; % HISTORY FILE
    H3 = [C1 C2 C3 C4 C5 C6]; % HISTORY FILE
    H4 = [D1 D2 D3 D4 D5 D6]; % HISTORY FILE
    
    H = cell(1,4); % MATRIX FOR ALL RETINA DATA
    H{1,1} = H1; H{1,2} = H2; H{1,3} = H3; H{1,4} = H4;
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
% JMP ANALYSIS FILES
%-------------------------------------------------------------------------%

%-------------------------------------------------------------------------%
F1 = xlsread('F1_JMP_Analysis_test3.xlsx'); % F1 JMP curve fitting
F2 = xlsread('C1_JMP_Analysis_new5.xlsx'); % C1 JMP curve fitting
F3 = xlsread('PufferK_JMP_Analysis_Test3.xlsx'); % PufferK curve fitting
F4 = xlsread('NemK_JMP_Analysis_new4.xlsx'); % NemK JMP curve fitting
JMP = cell(1,4);
JMP{1,1} = F1; JMP{1,2} = F2; JMP{1,3} = F3; JMP{1,4} = F4;
    
%=========================================================================%
    
%-------------------------------------------------------------------------%
% POST-PROCESS RETINA DATA
%-------------------------------------------------------------------------%
    
%=========================================================================%
    for index=1:4
        
        i = 1;
        j = 1;
        k = 1;
        t(1,1) = zeros;
        v(1,1) = zeros;
        V = []; 
        
        figure % creates figure first
        
        while k<=R{1,index}(end,1) % "50"
            
            if i+1<length(R{1,index}(:,1))
                
                while R{1,index}(i+1,1) == R{1,index}(i,1) && i+1<length(R{1,index}(:,1))
                    t(j) = R{1,index}(i,2); % time scale
                    v(j,1) = R{1,index}(i,3); % velocity vector 
                    i = i + 1;
                    j = j + 1;
                end
                V(:,k)=v; % velocity matrix for all 50 sets of data
            end
            
            %----------------------------%
            % Drop Breakup from ReTINA-X
            %----------------------------%
            for index_bu=1:length(R{1,index}(:,3))
                if R{1,index}(index_bu,3) ~= 0 
                    fprintf('drop leaves bore at time (us): ')
                    disp (R{1,index}(index_bu,2))
                    break
                end
            end
            
            t(j) = R{1,index}(i,2);
            l = i - ((length(t))-1);
            
            t = linspace(t(1),t(end),length(t));
            %             c = smooth(R{1,index}(l:i,3)); % smooth data
            %             c1 = reshape(c,length(R{1,index}(l:i,3)),1);
            
            % Calculate average and sd values for all sets of data
            
            set(gca,'Fontsize',16)
            p1 = plot(t,R{1,index}(l:i,3),'r.','MarkerSize',5);
            hold on
            
            [pks,locs] = findpeaks(R{1,index}(l:i,3));
              
            k=k+1;
            i=i+1;
            l=0;
            j=1;
            
        end
        
        % Average values & SD for DHV (m/s)
        %---------------------------------%
        V_avg(1,1) = zeros;
        V_std(1,1) = zeros;
        i = 1;
        
        while i<=length(V(:,1))
            V_avg(i) = mean(V(i,:));
            V_std(i) = std(V(i,:));
            i=i+1;
        end           
          
        [peaks,locations] = findpeaks(V_avg);
     
        e = (V_std')*(ones(size(t(1:74))));
        
%=========================================================================%
        
%-------------------------------------------------------------------------%
% POST-PROCESS BLD DATA
%-------------------------------------------------------------------------%

%=========================================================================%
        
%-----------------------------------%
% Calculate DHV from BLD data files
%-----------------------------------%
        
        % Set up time scale (extended) 
        %------------------------------%
        bld_end = t(1,:); 
        [~, bld_index] = min(abs(t(1,:)-t(end))); % time length distance
        closestValues = bld_end(bld_index);
        k_bld = find(abs(bld_end-closestValues) < 0.001);
        
        bld_time = linspace(0,t(k_bld),length(BLD{1,index}(:,1)));
        
        % Average BLD DHV Values
        %------------------------%
        bld_mean(1,2) = zeros;
        
        i=1;
        while i<= length(BLD{1,index}(:,1))
            bld_mean(i,1) = mean(BLD{1,index}(1:end,1));
            bld_mean(i,2) = mean(BLD{1,index}(1:end,2));
            i = i+1;
        end
        
        bld_1 = plot(bld_time,bld_mean(:,1),'--m','LineWidth',3.0);
        hold on
%         bld_2 = errorbar(R{1,index}(index_bu,2)+bld_time,bld_mean(:,1),bld_mean(:,2),':m');
%         hold on
        
        bld_mean = zeros(1,2); % Returns original value for bld_mean vector
        
%=========================================================================%
        
%-------------------------------------------------------------------------%
% POST-PROCESS CFD3 DATA
%-------------------------------------------------------------------------%
        
%=========================================================================%        
               
        % Filter disproportional values of history file (CFD3) for DHV
        
        %-----------------------------------%
        % Create velocity vector (CFD3 data)
        %-----------------------------------%
        
        time = H{1,index}(:,1); % set up new time scale
        time = linspace(time(1),time(end),length(time));
        
        i = 1; % rows of Velocity Matrix
        j = 1; % columns of Velocity Matrix
        k = 0; % DHV values of history file
        V1(i,j) = zeros;
        
        %-----------------------------------%
        % Creates Velocity Matrix from CFD3
        %-----------------------------------%
        
        while j <= 6
            
            while i <= length(H{1,index}(:,1))
                
                if H{1,index}(i,13+k) > 100 || H{1,index}(i,13+k) < 0
                    V1(i,j) = zeros;
                    
                else
                    V1(i,j)=H{1,index}(i,13+k);
                    
                end
                i = i+1;
            end
            j = j+1;
            i = 1;
            k = k+length(A1(1,:));
        end      
        
%-------------------------------------------------------------------------%
% Filters Development
%-------------------------------------------------------------------------%
        
        %-----------------%
        % Gaussian Filter                     
        %-----------------%                   
        
        V2 = zeros(size(V1));                 
        for i=1:length(V1(1,:))               
            g = gausswin(100); % Set up window size
            g = g/sum(g);
            V2(:,i) = conv(V1(:,i),g,'same');
        end
        
        V4 = zeros(size(V1));
        for i=1:length(V1(1,:))
            g = gausswin(50);
            g = g/sum(g);
            V4(:,i) = conv(V1(:,i),g,'same');
        end        
        
        %--------------------------------------%
        % Filter at every 7 values of DHV (m/s)   % What's the best filter?
        %--------------------------------------%
        i=1;
        j=1;
        k=1;
        V3(1,1) = zeros; % Different size from V1
        
        while k <= 6
            
            while i+7<=length(V1(:,1))
                
                V3(j,k)=mean(V1(i:i+7,k));      % Insert if statement later
                i = i+7;                        
                j = j+1;
                
            end
            k = k+1;
            i = 1;
            j = 1;
        end    
%-------------------------------------------------------------------------%
        
        %-----------------------------------------%
        % Creates Time Matrix from CFD3
        %-----------------------------------------%
        
        i = 1; % rows of Time Matrix
        j = 1; % columns of Time Matrix
        k = 0; % time values of history file
        T1(i,j) = zeros;
        
        while j <= 6
            
            while i <= length(H{1,index}(:,1))
                
                if H{1,index}(i,1+k) < 0 % Doesn't actually need...
                    T1(i,j) = zeros;
                    
                else
                    T1(i,j)=H{1,index}(i,1+k);
                    
                end
                i = i+1;
            end
            j = j+1;
            i = 1;
            k = k+length(A1(1,:));
        end
        
        t_end = T1(:,1);
        [~, index1] = min(abs(T1(:,1)-200));% Set index of final time value
        closestValues = t_end(index1);
        k_end = find(abs(t_end-closestValues) < 0.001);
        
        %------------------------------%
        % Time scale for 7-step filter
        %------------------------------%
        
        i = 1;
        j = 1;
        T2 = zeros(size(V3));
        
        while j<= 6
            T2(:,j) = linspace(T1(1),T1(k_end),length(V3(:,j)));
            j = j+1;
        end
        
%=========================================================================%

%-------------------------------------------------------------------------%
% PLOT ALL DATA (ReTINA, BLD, CFD3, JMP)
%-------------------------------------------------------------------------%

%=========================================================================%
        
        %--------%
        % ReTINA
        %--------%
        p2 = plot(t(1:74),V_avg,'-b','LineWidth',3.0);
        hold on
        p3 = errorbar(t(1:74),V_avg,e(:,1),':k');
        hold on
        
        %--------------%
        % JMP Analysis
        %--------------% 
        jmp = 1;
        V_JMP(1,1) = zeros;
        
        while jmp<=length(JMP{1,index}(:,13))
                if JMP{1,index}(jmp,13) > 100 || JMP{1,index}(jmp,13) < -100
                    V_JMP(jmp,1) = zeros;
                else
                    V_JMP(jmp,1) = JMP{1,index}(jmp,13);
                end
                jmp = jmp + 1;
        end
                
        time_jmp = linspace(JMP{1,index}(1,1),JMP{1,index}(end,1),length(V_JMP));            
        
        % Filter JMP
        %-----------%
        V_JMP2 = zeros(size(V_JMP));
        g = gausswin(100); 
        g = g/sum(g);
        V_JMP2(:,1) = conv(V_JMP(:,1),g,'same');
        
        [peaks_jmp,locs_jmp] = findpeaks(V_JMP2);
        
        j1 = plot(R{1,index}(index_bu,2)+time_jmp,V_JMP2,'-m','LineWidth',2.0);
        hold on
               
        V_JMP = []; % Necessary to fit time scale
        
        %------------------%
        % CFD3 Simulations
        %------------------%
        time = linspace(T1(1),T1(k_end),length(V2));
        
        for i=1:length(T1(1,:))
            
            if i==1
                p4 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'-k',...
                    'LineWidth',2.0); % GAUSSIAN FILTER 100
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'-k',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER 50
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-r',...
%                'LineWidth',1.0);      % RAW DATA
            end
            
            if i==2
                p5 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'-c',...
                    'LineWidth',2.0); % GAUSSIAN FILTER
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'-c',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-g',...
%                'LineWidth',1.0);      % RAW DATA
           
            end
            
            if i==3                
                p6 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'-g',...
                    'LineWidth',2.0); % GAUSSIAN FILTER
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'-g',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-r',...
%                'LineWidth',1.0);      % RAW DATAA Compare filtered with noisy data
                
            end
            
            if i==4
                p7 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'--k',...
                    'LineWidth',2.0); % GAUSSIAN FILTER
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'--w',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-r',...
%                     'LineWidth',1.0);      % RAW DATA

            end
            
            if i==5
                p8 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'--c',...
                    'LineWidth',2.0); % GAUSSIAN FILTER
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'--c',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-r',...
%                'LineWidth',1.0);      % RAW DATA
          
            end
            
            if i==6
                p9 = plot(R{1,index}(index_bu,2)+T1(1:k_end,i),V2(1:k_end,i),'--g',...
                    'LineWidth',2.0); % GAUSSIAN FILTER
%               plot(A(index_bu,2)+T1(1:k_end,i),V4(1:k_end,i),'--g',...
%                     'LineWidth',2.0); % GAUSSIAN FILTER
%                 test = plot((A(index_bu,2))+T2(:,i),V3(:,i),'--r',...
%                     'LineWidth',1.0); % 7-STEP FILTER
%                 test2 = plot(A(index_bu,2)+T1(1:k_end,i),V1(1:k_end,i),'-r',...
%                'LineWidth',1.0);      % RAW DATA
                
            end
            
        end
        
%=========================================================================%        
               
%-------------------------------------------------------------------------%
% DYNAMIC SURFACE TENSION
%-------------------------------------------------------------------------%
        
%=========================================================================%

%-------------------------------------------------------------------------%
% ReTINA-X Surface Tension Estimate
%-------------------------------------------------------------------------%
        
% To determine the surface tension it is essential that the weight of the
% drop head is accurate. The surface tension estimate is based on the
% radius of the main drop head and therefore its weight measurement is
% necessary. BLD/ReTINA data was gathered but there is no method to
% accurately determine the weight just for the drop head. An approximation
% of 70% - 80% of the whole drop weight was used but the values can be
% substantially different. THE MODEL IS VERY SENSITIVE TO THESE VALUES.
        
        if index == 1
            retina_DW = (10.^-15.)*[8.758]; % what percentage on DH?
        end
        
        if index == 2
            retina_DW = (10.^-15.)*[4.5]; % 
        end
        
        if index == 3
            retina_DW = (10.^-15.)*[0]; %
        end
        
        if index == 4
            retina_DW = (10.^-15.)*[6.0]; %
        end
        
        retina_radius = (((3/4)*(retina_DW))/(pi))^(1./3.); % meters
        
        retina_density = 1000; % kg/m^3
        
        retina_oscillation = t(locations(5)) - t(locations(4)) % us
        
        retina_oscillation = retina_oscillation*(10.^-6.); % s
        
        retina_frequency = (2*pi)/(retina_oscillation); % rad/us
        
        retina_viscosity = (0.75)*(10^-3); % cP -> Pa*s
        
        retina_decay = (10^6)*(((retina_density)*(retina_radius^2))/(5*retina_viscosity)); % seconds
        
        retina_frequency_corrected = (retina_frequency)*((1 - ((retina_frequency)*(retina_decay))^(-2))^(1/2));
        
        retina_ST = ((((((2*pi)^2))*retina_density)*((retina_radius)^3))/((8)*retina_oscillation^2))*1000. % N/m -> dyne/cm
                        
        % ReTINA-X Peaks
        %----------------%
        plot(t(locations(5)),peaks(5),'ks','MarkerSize',10.0)
        hold on
        plot(t(locations(4)),peaks(4),'ks','MarkerSize',10.0)
        hold on 
        
%-------------------------------------------------------------------------%        
% CFD3 Surface Tension Estimate
%-------------------------------------------------------------------------%
        
        % Viscosity (nominal values)
        %---------------------------%
        if index == 1
            viscosity = (0.8)*(10^-3); % cP -> Pa*s (F1 Surfactant)
        end
        
        if index == 2
            viscosity = (0.7)*(10^-3); % cP -> Pa*s (C1 Surfactant)
        end
        
        if index == 3
            viscosity = (1.0)*(10^-3); % cP -> Pa*s (PufferK)
        end
        
        if index == 4
            viscosity = (1.4)*(10^-3); % cP -> Pa*s (NemesisK)
        end
        
% The drop weight values below were manually extracted by observing the 
% satellite simulation from the main CFD3 page on the DME environment. The
% drop weight values are referred to the drop head only in order to more
% precisely describe the surface tension through the analytical equation.
% The values in the matrices below represent 24 sets of experiments: all
% the factorials for 4 different values of Vcrit (0.25 - 1.00) and 2
% different values of Pfloor (1e5 & 5e5) to 3 different values of surface
% tension (20, 40 70).
        
        % Drop Weight (F1 Surfactant Series)    
        %-----------------------------------%
        if index == 1 
            drop_weight = (10.^-15.)*(1.0)*... 
                [1.74 2.20 2.57 3.45 3.03 3.64;...  % Vcrit = 0.25
                3.62 5.20 4.33 5.00 5.08 5.06;...   % Vcrit = 0.50
                5.37 6.00 6.25 5.80 6.54 6.91;...   % Vcrit = 0.75
                5.90 6.13 7.10 6.29 6.01 7.54];     % Vcrit = 1.00
            % pL -> m^3 % Set this up for the rest
        end
        
        % Drop Weight (C1 Surfactant Series)
        %-----------------------------------%
        if index == 2  
            drop_weight = (10.^-15.)*(1.0)*... 
                [1.81 2.23 2.60 3.47 3.02 3.13;...  % Vcrit = 0.25
                4.63 5.27 4.39 4.99 5.55 5.16;...   % Vcrit = 0.50
                5.43 6.03 6.35 5.83 6.53 7.00;...   % Vcrit = 0.75
                5.90 5.89 7.10 6.29 6.07 7.48];     % Vcrit = 1.00
            % pL -> m^3 % Set this up for the rest
        end
        
        % Drop Weight (Puffer K Series)
        %-----------------------------------%
        if index == 3  
            drop_weight = (10.^-15.)*(1.0)*... 
                [1.78 2.18 2.52 2.43 2.97 3.02;...  % Vcrit = 0.25
                3.41 5.18 4.26 3.88 4.94 5.00;...   % Vcrit = 0.50
                5.37 5.92 6.20 5.77 6.50 6.82;...   % Vcrit = 0.75
                5.92 5.76 7.09 6.31 5.21 7.51];     % Vcrit = 1.00
            % pL -> m^3 % Set this up for the rest
        end
        
        % Drop Weight (Nemesis K Series)
        %-----------------------------------%
        if index == 4  
            drop_weight = (10.^-15.)*(1.0)*... 
                [1.84 2.14 2.56 2.39 2.85 3.55;...  % Vcrit = 0.25
                3.21 4.04 4.21 3.71 4.69 4.92;...   % Vcrit = 0.50
                4.31 5.86 6.16 4.61 6.41 6.75;...   % Vcrit = 0.75
                5.99 5.47 7.05 6.36 6.63 7.52];     % Vcrit = 1.00
            % pL -> m^3 % Set this up for the rest
        end
              
        % Set up the peak values of oscillation
        %--------------------------------------%
        for i=1:length(V2(1,:))
            [pks,locs] = findpeaks(V2(:,i));
            
            % Plot the corrected values for the peaks of each Vcrit
            %-------------------------------------------------------%
            vcrit_value=1; %start Vcrit value == 1 -----> Vcrit =0.25
            
            peak_value=4; %start Peak value == 3 + 2 (5) - 3+1 (4) for Vcrit=0.25
            
            while peak_value >= 1
                if vcrit == vcrit_value
                    oscillation = T1(locs(peak_value+2),i)-T1(locs(peak_value+1),i)
                    add = 1;
                    % Correct the peak values identified (needs improvement)
                    %------------------------------------%
                    if oscillation < 5
                        while oscillation < 5
                            oscillation = T1(locs(peak_value+2+add),i)-T1(locs(peak_value+1),i)
                            plot(R{1,index}(index_bu,2)+T1(locs(peak_value+2+add),i), V2(locs(peak_value+2+add),i),'ks','MarkerSize',10.0)
                            plot(R{1,index}(index_bu,2)+T1(locs(peak_value+1),i), V2(locs(peak_value+1),i),'ks','MarkerSize',10.0)
                            add = add + 1;
                        end
                    else
                        plot(R{1,index}(index_bu,2)+T1(locs(peak_value+2),i), V2(locs(peak_value+2),i),'ks','MarkerSize',10.0)
                        plot(R{1,index}(index_bu,2)+T1(locs(peak_value+1),i), V2(locs(peak_value+1),i),'ks','MarkerSize',10.0)                     
                    end
                end
                peak_value = peak_value-1;
                vcrit_value = vcrit_value+1;
            end
                        
            oscillation = oscillation.*(10.^-6.); % Conversion us -> s  
            
            DW = (10^15)*drop_weight(vcrit,i);
            
            drop_radius = (((3/4)*(drop_weight(vcrit,i)))/(pi))^(1./3.); % meters
            
            diameter = 2*(10^6)*drop_radius; % meter->um
            
            density = 1000; % Set this value later kg/(m^3)
            
            surface_tension = ((((((2*pi)^2))*density)*((drop_radius)^3))/((8)*oscillation^2))*1000. % N/m -> dyne/cm
            
            frequency = (2*pi)/(oscillation); % ANGULAR rad/us
                        
            decay = (((density)*(drop_radius^2))/(5*viscosity))*(10^6); % micro-seconds
            
            frequency_corrected = (frequency)*((1 - ((frequency)*(decay))^(-2))^(1/2));
                    
            ST = (1./1000.)*[20 40 70 20 40 70; ...
                             20 40 70 20 40 70; ...
                             20 40 70 20 40 70; ...
                             20 40 70 20 40 70]; % Surface tension range of values -> dyne/cm -> N/m
                            
            oscillation_analytical = (10.^6.)*((((((2*pi)^2)*density)*((drop_radius)^3))/((8)*ST(vcrit,i)))^(1./2.)) % s-> us
        
        end
        
%-------------------------------------------------------------------------%        
% JMP Analysis Surface Tension Estimate
%-------------------------------------------------------------------------%
         jmp_density = 1000;
         
         if index == 1
             jmp_DW = (10.^-15.)*[4.93]; %F1 (drop head weight)
         end
         
         if index == 2
             jmp_DW = (10.^-15.)*[3.95]; %C1 (drop head weight)
         end
         
         if index == 3
             jmp_DW = (10.^-15.)*[6.89]; %PufferK (drop head weight)
         end
         
         if index == 4
             jmp_DW = (10.^-15.)*[5.97]; %NemK (drop head weight)
         end
         
         jmp_radius = (((3/4)*(jmp_DW))/(pi))^(1./3.); % meters        

         jmp_oscillation = time_jmp(locs_jmp(3)) - time_jmp(locs_jmp(2))
         
         jmp_oscillation = jmp_oscillation*(10.^-6.);
         
         plot(R{1,index}(index_bu,2)+time_jmp(locs_jmp(2)),peaks_jmp(2),'ks','MarkerSize',10.0)
         
         plot(R{1,index}(index_bu,2)+time_jmp(locs_jmp(3)),peaks_jmp(3),'ks','MarkerSize',10.0)
         
         JMP_ST = ((((((2*pi)^2))*jmp_density)*((jmp_radius)^3))/((8)*jmp_oscillation^2))*1000.
         
%=========================================================================%        
               
%-------------------------------------------------------------------------%
% LEGEND ENTRIES
%-------------------------------------------------------------------------%
        
%=========================================================================%
        l1 = legend([p1 p2 bld_1 p4 p5 p6 p7 p8 p9 j1],...
            {'ReTINA Data', 'ReTINA (avg velocity)', 'BLD (Corvallis)',...
            '$\gamma = 20(d/cm)$ Pf = 1e5',...
            '$\gamma = 40(d/cm)$ Pf = 1e5',...
            '$\gamma = 70(d/cm)$ Pf = 1e5',...
            '$\gamma = 20(d/cm)$ Pf = 5e5',...
            '$\gamma = 40(d/cm)$ Pf = 5e5',...
            '$\gamma = 70(d/cm)$ Pf = 5e5',...
            'JMP Fit Analysis'},'Interpreter','LaTex');
        set(l1,'FontSize',14)
        hold on
        
        %-------------------%
        % Set up plot title                 % Set up this to be interactive
        %-------------------%
        
        if vcrit == 1
                if index==1
                    title({'F1 Surfactant Series ($V_{crit}=0.25$)'},'Interpreter','LaTex');
                end
                
                if index==2
                    title({'C1 Surfactant Series ($V_{crit}=0.25$)'},'Interpreter','LaTex');
                end
                
                if index==3
                    title({'Puffer K ($V_{crit}=0.25$)'},'Interpreter','LaTex');
                end
                
                if index==4
                    title({'Nemesis K Series ($V_{crit}=0.25$)'},'Interpreter','LaTex');
                end
            end
            
            if vcrit == 2
                if index==1
                    title({'F1 Surfactant Series ($V_{crit}=0.50$)'},'Interpreter','LaTex');
                end
                
                if index==2
                    title({'C1 Surfactant Series ($V_{crit}=0.50$)'},'Interpreter','LaTex');
                end
                
                if index==3
                    title({'Puffer K ($V_{crit}=0.50$)'},'Interpreter','LaTex');
                end
                
                if index==4
                    title({'Nemesis K Series ($V_{crit}=0.50$)'},'Interpreter','LaTex');
                end
            end
               
            if vcrit == 3
                if index==1
                    title({'F1 Surfactant Series ($V_{crit}=0.75$)'},'Interpreter','LaTex');
                end
                
                if index==2
                    title({'C1 Surfactant Series ($V_{crit}=0.75$)'},'Interpreter','LaTex');
                end
                
                if index==3
                    title({'Puffer K ($V_{crit}=0.75$)'},'Interpreter','LaTex');
                end
                
                if index==4
                    title({'Nemesis K Series ($V_{crit}=0.75$)'},'Interpreter','LaTex');
                end
            end
            
            if vcrit == 4
                if index==1
                    title({'F1 Surfactant Series ($V_{crit}=1.0$)'},'Interpreter','LaTex');
                end
                
                if index==2
                    title({'C1 Surfactant Series ($V_{crit}=1.0$)'},'Interpreter','LaTex');
                end
                
                if index==3
                    title({'Puffer K ($V_{crit}=1.0$)'},'Interpreter','LaTex');
                end
                
                if index==4
                    title({'Nemesis K Series ($V_{crit}=1.0$)'},'Interpreter','LaTex');
                end
            end
        
        xlim([0 t(74)]);
        ylim([0 20]);
        x1=xlabel('Time (\mus)');
        set(x1,'FontSize',16)
        y1 = ylabel('DHV (m/s)');
        set(y1,'FontSize',16)
        
    end
end
%-------------------------------------------------------------------------%

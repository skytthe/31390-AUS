close all
clear all
clc
clear classes
%% Setup the map 
% Define the map size
max_x = 10;
max_y = 10;
max_z = 10;
map = zeros(max_x, max_y, max_z);

% Define the starting and end position
start = [1, 1, 1];
end_ = [10, 10, 10];

% Make sure the start and end is not an obstacle
map(start(1), start(2), start(3)) = 0;
map(end_(1), end_(2), end_(3)) = 0;

% Add obstacles
map = gen_square3d([2 3; 1 10; 1 11], map);
map = gen_square3d([4 5; 2 11; 1 11], map);
map = gen_square3d([6 7; 1 8; 1 11], map);
map = gen_square3d([6 7; 9 11; 1 11], map);
map = gen_square3d([6 7; 8 9; 1 8], map);
map = gen_square3d([6 7; 8 9; 9 11], map);
map = gen_square3d([8 9; 2 11; 1 11], map);

%% Run the algorithm to optain the route
ena_route = false;
draw_ena = true;

if ena_route
    route = greedy_3d(map, start, end_);
else
    route = [[1,1,1];[1,2,1];[1,2,2]];
end

%% Run the algorithm to optain the route


pe = pyenv;
if pe.Status == 'Loaded'
    %disp('To change the Python version, restart MATLAB, ')
else
    pyenv('Version','/usr/bin/python3');
end


search_alg = py.importlib.import_module('map_search_algorithms');
py.importlib.reload(search_alg);

map_1d = reshape(map,1, []);

search_res = search_alg.search_BFS(py.list(map_1d), py.list(start), py.list(end_));

%reshape to matlab format
cP = cell(search_res);
A = cellfun(@double,cP);
route_BFS = reshape(A.',3,[]).';

search_res = search_alg.search_Greedy(py.list(map_1d), py.list(start), py.list(end_));

%reshape to matlab format
cP = cell(search_res);
A = cellfun(@double,cP);
route_Greedy = reshape(A.',3,[]).';

search_res = search_alg.search_Astar(py.list(map_1d), py.list(start), py.list(end_));

%reshape to matlab format
cP = cell(search_res);
A = cellfun(@double,cP);
route_Astar = reshape(A.',3,[]).';

%route = route_BFS;
%route = route_Greedy;
route = route_Astar;

%% Draw the map
if draw_ena

    % Draw a figure to show the map and process
    hold off
    figure(1)
    % Mark the start with green
    scatter3(start(1)+0.5, start(2)+0.5, start(3)+0.5, ...
             500, [0,1,0],'filled')
    hold on

    % Mark the end with red
    scatter3(end_(1)+0.5, end_(2)+0.5, end_(3)+0.5, ...
             500, [1,0,0], 'filled')
    hold on

    % Draw the obstacles
    map = gen_square3d([2 3; 1 10; 1 11], map, 1);
    map = gen_square3d([4 5; 2 11; 1 11], map, 1);
    map = gen_square3d([6 7; 1 8; 1 11], map, 1);
    map = gen_square3d([6 7; 9 11; 1 11], map, 1);
    map = gen_square3d([6 7; 8 9; 1 8], map, 1);
    map = gen_square3d([6 7; 8 9; 9 11], map, 1);
    map = gen_square3d([8 9; 2 11; 1 11], map, 1);

    % Set the axes
    axis([1 max_x+1 1 max_y+1 1 max_z+1])
    % Make the grid lines more visible
    ax = gca;
    ax.GridAlpha = 1.0;
    grid on
    set(gca, 'xtick', [0:1:max_x])
    set(gca, 'ytick', [0:1:max_y])
    set(gca, 'ztick', [0:1:max_z])

    % Draw the route
    pause on;
    for i = 2:length(route)
        plot3([route(i-1,1)+0.5,route(i,1)+0.5], ...
              [route(i-1,2)+0.5,route(i,2)+0.5], ...
              [route(i-1,3)+0.5,route(i,3)+0.5], ...
              'color',[0,0,0],'linewidth',5)
        hold on
        pause(0.1)
        route(i,:);
    end

    hold off
end
#!/usr/bin/env bash

name=discworld

tmux new-session -d -s $name
tmux rename-window "$name"

# split it vertically 50%
tmux split-window -h -p 50

# select left pane and split it horizontally 85%
tmux select-pane -t 0
tmux split-window -v -p 85

tmux send-keys -t 0 "tail -f logs/chat.log" "Enter"
tmux send-keys -t 1 "make run" "Enter"

tmux -2 attach-session -t $name

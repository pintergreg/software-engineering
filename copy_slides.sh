#!/usr/bin/bash
mkdir -p book/slides/figures
mkdir -p book/slides/assets
cp -r lectures/figures/* book/slides/figures/
cp -r lectures/*.html book/slides/
cp -r assets/* book/assets/

set terminal pdf
set output "ProposedLength.pdf"
set style data histogram
set key auto column
set yrange [0:*] noextend
set tics nomirror
set border 3
set offset 0,0,2,0
set bmargin 5

set xlabel "" font ",12"
set ylabel "Average Path Length" font ",12"
# set xtics font ",15" # Increased font size for xtics
set xtics format ""
set ytics font ",15" # Increased font size for ytics

set boxwidth 1
set style histogram clustered gap 1.4

set style fill solid border -1
set style histogram errorbars lw 2
set datafile columnhead separator whitespace

# To move the Baseline and Proposed left of the screen
set key left

plot 'dataL.dat' using 1:2 fs solid 0.5 lw 2 ti 'Traditional', \
     '' using 3:4 fs solid 0.0 lw 2 ti 'Proposed'

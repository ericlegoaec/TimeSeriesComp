The_Bench_Grower - Benchmarking and Growth of a Dollar Package
==============================================================

The_Bench_Grower - which stands for a combination of Benchmarking and Growth of a Dollar analysis - is a package 
designed to help any financial analyst by providing a scalable tool for use alongside today's standard 
data-import tool: Bloomberg. Written by Jameson Lee and John Pugliesi, The_Bench_Grower operates in
the following manner:

Using the excel add-in (from within Bloomberg) to download real total return (net dividends) values across a range of
indeces and securities, The_Bench_Grower is able to:
 - Calculate the corresponding performance data (on whatever date style is used i.e. days, months, years... etc.)
 - Determine the Growth of a Dollar value of the security over time
 - Plot the corresponding Growth of a Dollar time series within your browser
 - Determine the excess return of a list of securities relative to a (for now) single benchmark
 - Plot the excess return of each security (relative to said benchmark) within your browser

BUT HOW DO I USE THE_BENCH_GROWER?
Using Bloomberg's excel add-in:
 1. Make sure that your first ticker-value is your benchmark.
 2. Add as many values as you'd like thereafter.
 3. Select the option within Bloomberg for "real total return (net dividends)"
 4. Specify your date range
 5. Complete the Excel Add-in process:
 	5.1. Copy-paste the values as values, and save the file as a csv where you will place it on the desktop
 6. Open up "The_Bench_Grower" in your respective IDE. (We used Sublime text...)
 7. Run the main.py file, and from the main menu, specify the file on your desktop!

Please comment on our github to provide feedback and let us know how we can improve The_Bench_Grower in the future!

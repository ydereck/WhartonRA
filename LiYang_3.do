clear
*change directory if needed
*cd "C:\Users\Data Task\Wharton_Zhu_Zhou\T3"
use InconsistentDisclosures

* Calculate fraction of inconsistent disclosures where inconsistent=1 by primary category
egen inconsistent_1 = total(inconsistent==1), by(primarycategory)
egen total_obs = count(inconsistent), by(primarycategory)
gen frac_inconsistent = inconsistent_1 / total_obs if total_obs > 0

* Calculate mean performance by primary category
collapse (mean) performance1 frac_inconsistent, by(primarycategory)

* Export the 1st table to Excel
export excel primarycategory frac_inconsistent performance1 using LiYang_3.xlsx, sheet("Tab1") replace firstrow(variables)
putexcel set LiYang_3, modify sheet("Tab1")
putexcel A1 = "Category" B1 = "Fraction" C1 = "Performance"
putexcel (B2:B12), nformat("percent_d2")
putexcel (C2:C12), nformat("percent_d2")

save t1, replace

* Load the data again for the summary by year
use InconsistentDisclosures
gen year = year(date)

* Calculate fraction of inconsistent disclosures where inconsistent=1 by primary category
egen inconsistent_2 = total(inconsistent==1), by(year)
egen total_obs_2 = count(inconsistent), by(year)
gen frac_inconsistent_2 = inconsistent_2 / total_obs_2 if total_obs_2 > 0

collapse (mean) performance1 frac_inconsistent_2, by(year)

* Put the summary stats into a Matrix
matrix results_2 = J(6,3,.)
forvalues i = 1/6 {
	matrix results_2[`i',1]=year[`i']
	matrix results_2[`i',2]=frac_inconsistent_2[`i']
	matrix results_2[`i',3]=performance1[`i']
}

*Continue writing the 2nd table to Excel
putexcel E1 = "Year" F1 = "Fraction" G1 = "Performance"
putexcel E2 = matrix(results_2)
putexcel (A1:G1), bold
putexcel (F2:F12), nformat("percent_d2")
putexcel (G2:G12), nformat("percent_d2")
save t2, replace

* Load the data again for OLS
use InconsistentDisclosures
gen year = year(date)

putexcel set LiYang_3.xlsx, sheet(Tab2) modify
quietly reg performance1 inconsistent i.year

* Export the regression results to a new tab
matrix table = r(table)
matrix results_3 = table[1..4,1...]'
putexcel B1="Ceof." C1="se" D1="t-stat" E1="p-value"
putexcel A2=matrix(results_3), rownames
putexcel A10 = "N=", italic right
putexcel A11 = "R-sq=", italic right
putexcel B10 = matrix(e(N)) B11 = matrix(e(r2))
putexcel (A1:E1), bold
putexcel (A2:A9), bold
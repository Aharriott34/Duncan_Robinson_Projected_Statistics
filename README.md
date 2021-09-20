# Duncan_Robinson_Projected_Statistics

Description:

Duncan Robinson is a current NBA player that plays for the Miami Heat. He is cuurrently an elite three point shooters in the league, and recently resigned with the Miami Heat for five more seasons. A question was raised with his new contract, is he on track to crack the top five in three point shots made? This code and visualizations will answer that question, barring he has a heathy season, and there aren't any lockuts in the near future. All statistics were taken from basketball-reference.com, and nba.com.

Built With:

- PostgreSQL
- Python 3
- Power BI

Python packages used for analyzation:

- Numpy
- Scipy.stats
- Random
- Collections.abc


Python packages for visualization:

- Matplotlib
- Seaborn


Visualizations:
- This first chart shows the top five NBA players that have made the most amount of three point shots. Out of the five, Stephen Curry and James Harden are the only players currently playing in the NBA. Ray Allen played from 1996-2014, Reggie Miller played from 1987-2004, and Kyle Korver played from 2003-2019.
![Top 5 Total](https://user-images.githubusercontent.com/78121835/133536846-ea62d24e-9e66-4769-a534-0569a8687f47.png)
- A boxplot was created to show the distribution for each of the shooters for their first eight seasons. Stephen Curry had the highest IQR and median out of the five, and Kyle Korver was the only player that had an outlier.
![Top 5 Shooters Boxplot](https://user-images.githubusercontent.com/78121835/133536857-4bc957d0-d312-4a46-9fd3-ddd74cd8fff9.png)
- A violinplot was then made to find the full distribution for the players. All players have a unimodal(bell-shaped) curved however, some varied in skew. The violinplot also displays how far Stephen Curr'y's quartiles strech out.
![Top 5 Shooters Violinplot](https://user-images.githubusercontent.com/78121835/133536877-ad572256-7a29-4f77-9000-8c3321b630f3.png)
- Now getting into Duncan Robinson, this histogram displays how many three point shots he can make in a season. Duncan has not played a full 82 game season yet due to the COVID-19 shortening two out of his three seasons. That being said, if he plays a full 82 game season, a sample size was created to show how many threes he will make with his three point percentage slightly increased. A size of 612 threes attempted, 264 made, with a 42.9% probability of him making the shot.
![Duncan Robinson Histogram](https://user-images.githubusercontent.com/78121835/133536888-e964b76f-eb7f-4168-bb33-10e84061533e.png)
- With the histogram created, the next 5 seasons can be projected. Duncan did not get much playing time in his first year, hence a low amount of shots made. 
![Duncan Robinson Season Projection](https://user-images.githubusercontent.com/78121835/133536901-44b7fb4c-d1e5-4afa-bd30-e5ac48c26b6d.png)
- Now with the next 5 seasons projected, there can be a forecast of the total amount of three pointers made for the first 8 seasons. The forecast can now be compared against the top 5 players in their first 8 seasons.
![Duncan vs Top 5](https://user-images.githubusercontent.com/78121835/133536919-6a611f0d-f77c-4385-99d3-5ea923040120.png)


Power BI:
- A Power BI dashboard was created to visualize Duncan's offensive stastics for his first three years playing. It can filter out his stats by opponents, if he played at home or away, and if the Miami Heat won or lost the game. The dashboard file is available above.
<img width="614" alt="Power BI Dashboard" src="https://user-images.githubusercontent.com/78121835/133543212-08f6f3b9-3def-493d-a63e-36d6a8a458bd.png">


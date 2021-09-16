# Duncan_Robinson_Projected_Statistics

Description:

Duncan Robinson is a current NBA player that plays for the Miami Heat. He is cuurrently an elite three point shooters in the league, and recently resigned with the Miami Heat for five more seasons. A question was raised with his new contract, is he on track to crack the top five in three point shots made? This code and visualizations will answer that question, barring he has a heathy season, and there aren't any lockuts in the near future. All statistics were taken from basketball-reference.com, and nba.com.

Built With:

PostgreSQL
Python 3
Power BI
Prerequisites:

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
![Top 5 Shooters Total](https://user-images.githubusercontent.com/78121835/133533229-a9fa6070-59a1-42e2-a0df-96a14d7cd29b.png)
- A boxplot was created to show the distribution for each of the shooters for their first eight seasons. Stephen Curry had the highest IQR and median out of the five, and Kyle Korver was the only player that had an outlier.
![Top 5 Shooters Boxplot](https://user-images.githubusercontent.com/78121835/133533554-cfeba905-0e4f-4053-a808-769669a9a641.png)
- A violinplot was then made to find the full distribution for the players. All players have a unimodal(bell-shaped) curved however, some varied in skew. The violinplot also displays how Stephen Curr'y's quartiles strech out to.
![Top 5 Shooters Violinplot](https://user-images.githubusercontent.com/78121835/133534652-bd9bc671-2737-4b38-83b1-135f9d778acc.png)
- Now getting into Duncan Robinson, this histogram displays how many three point shots he can make in a season. Duncan has not played a full 82 game season yet due to the COVID-19 shortening two out of his three seasons. That being said, if he plays a full 82 game season, a sample size was created to show how many threes he will make with his three point percentage slightly increased. A size of 612 threes attempted, 264 made, with a 42.9% probability of him making the shot.
![Duncan Robinson Histogram](https://user-images.githubusercontent.com/78121835/133535304-773f0322-5920-4c72-bf44-f46a5a7245ef.png)





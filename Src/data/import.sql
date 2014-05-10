

CREATE TABLE Players(

    Country TEXT,
    Postion TEXT,
    Jersey  TEXT,
    Player  TEXT,
    Url     TEXT

);

CREATE TABLE Replacements(

    Country      TEXT,
    Time         TEXT,
    Original     TEXT,
    Replacements TEXT,
    Url          TEXT

);

CREATE TABLE Main(

    Event               TEXT,
    Event_Url           TEXT,
    Results             TEXT,
    Results_Url         TEXT,
    Playoffs            TEXT,
    Playoffs_Url        TEXT,
    Top_Scorers         TEXT,
    Top_Scorers_Url     TEXT,
    Final_Standings     TEXT,
    Final_Standings_Url TEXT
    
);

CREATE TABLE Overview(

    Country TEXT,
    Stats   TEXT,
    Url     TEXT

);

CREATE TABLE Match_results(

    Team1              TEXT,
    Team2              TEXT,
    Goals_Team1        TEXT,
    Goals_Team2        TEXT,
    Goal_Scorers_Team1 TEXT,
    Goal_Scorers_Team2 TEXT,
    Url                TEXT

);

CREATE TABLE Cards(

    Country TEXT,
    Player  TEXT,
    Card    TEXT,
    Url     TEXT

);

CREATE TABLE Results(

    Game_Number TEXT,
    Team1       TEXT,
    Team2       TEXT,
    Score       TEXT,
    Game_Url    TEXT,
    Group_Name  TEXT,
    Group_Url   TEXT

);

CREATE TABLE Group_Results(

    Game_Number   TEXT,
    Country       TEXT,
    Pts           TEXT,
    Gp            TEXT,
    W             TEXT,
    D             TEXT,
    L             TEXT,
    Gs            TEXT,
    Ga            TEXT,
    Gd            TEXT,
    Qualification TEXT, 
    Url           TEXT

);

.separator ','
.import players.csv Players
.import replacements.csv Replacements
.import mainfile.csv Main
.import overview.csv Overview
.import matchresults.csv Match_results
.import cards.csv Cards

.separator '|'
.import results.csv Results
.import groupresults.csv Group_Results

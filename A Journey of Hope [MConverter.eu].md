# ![](media/image2.jpeg){width="1.8732392825896762in" height="4.2in"}  {#section}

# Table of Contents {#table-of-contents .TOC-Heading}

[Introduction: [2](#introduction)](#introduction)

[Game Story: [2](#game-story)](#game-story)

[Gameplay mechanics: [3](#gameplay-mechanics)](#gameplay-mechanics)

[Specific goal of the game:
[3](#specific-goal-of-the-game)](#specific-goal-of-the-game)

[Game launch and Initial setup:
[3](#game-launch-and-initial-setup)](#game-launch-and-initial-setup)

[Game Rules: [3](#game-rules)](#game-rules)

[Game flow: [4](#game-flow)](#game-flow)

[Score calculation: [4](#score-calculation)](#score-calculation)

[Data Storage: [5](#data-storage)](#data-storage)

[Further Development Ideas:
[5](#further-development-ideas)](#further-development-ideas)

A Journey of Hope

# Introduction:

**A Journey of Hope** is a text-based travel game where player takes on
a role of a traveller who navigates through the airports around the
world. The player must visit a maximum number of airports with a minimum
carbon footprint. In this game, the player must combine the elements of
strategy, resource management, and decision making.  
**Game Overview:**

- Type: Single Player, Travel Game, Strategy Formulation and Execution

- Console: Python Console

- Target Audience: All age-groups above twelve years who are interested
  in strategic games.

# Game Story:

The main three characters in the game are cancer patients who
coincidently met at the same hospital for their treatment. Since all of
them are in the process of curing their disease, they begin to have
conversations with each other about their situation and how they caught
cancer. After a brief conversation with each other, they realized that
all three of them want to make the rest of their lives meaningful by
travelling to places they always wanted to. However, they are also aware
that environmental pollution is the root cause of increasing cancer in
people. So, they produce an idea that they will try their best to limit
their co2 consumption to the lowest while also travelling to as many
places as possible within their budget and fuel.

![](media/image3.jpg){width="4.8037970253718285in"
height="2.031645888013998in"}

# Gameplay mechanics:

## Specific goal of the game:

The main goal of this game is to travel through all the designated
airports using the shortest path possible while emitting lowest possible
amount of CO2 and saving as much fuel and money as possible. Every
decision is important to achieve a higher score in this eco-friendly
challenge.

## Game launch and Initial setup:

- **Player Name:** Player enters their chosen name.

- **Starting Point:** Helsinki Vantaa Airport (EFHK)

- **Airport List:** Program provides randomly generated list of 12
  airports from medium and large airports in the database. Or the player
  can also use the airport list used by the previous player.

- **Difficulty Levels:**

1.  Easy (Henderson): Player gets \$3000 to start the game.

2.  Medium (Rosaline): Player gets \$2000 to start the game.

3.  Hard (Josh): Player gets \$1000 to start the game.

- **Difficulty Multiplier:**

  1.  Easy: 1

  2.  Medium: 2

  3.  Hard: 3

- **Fuel, CO2 emissions and Hints:** For all difficulty levels initial
  fuel is 1000 liters, CO2 emissions is 0kg and the player gets 3 hints
  to receive information about the nearest airport.

## Game Rules:

- **Traveling**:

  - Players must select from the list of available airports.

  - Distance traveled affects fuel consumption and CO2 emissions.

- **Fuel**:

  - Running out of fuel ends the game.

  - Players can purchase additional fuel if they have sufficient money.

- **Money**:

  - Player can use money for purchasing additional fuel and hints.

- **Hints**:

  - Hints are used to receive information on the nearest airport.

  - Player can purchase additional hints with the money.

- **Ending the Game**:

  - The game ends when the player chooses to stop traveling or runs out
    of fuel or has travelled all the airports.

- **Rewards**:

  - Player receives 100 liters of fuel after visiting every third
    airport.

# Game flow:

> The game's progression is represented in the diagram below:![fig.1:
> Game flow diagram.](media/image5.jpg){width="6.5in"
> height="3.567361111111111in"}

Figure 1: Game flow diagram.

# Score calculation:

The player's final score is calculated by using following formula:

![A black text on a white background Description automatically
generated](media/image6.png){width="3.6455697725284337in"
height="0.640505249343832in"}

# Data Storage:

The database named flight_game is used in the game to fetch airport
information for gameplay, storing of player scores and retrieving
previous players' airport list. The Entity Relationship Diagram of the
database used in the game is presented below:

![](media/image7.png){width="6.313560804899388in"
height="3.4367082239720035in"}

Figure 2: ER diagram of the flight_game database used in the game.

# Further Development Ideas:

- Include graphical user interface to make the game visually appealing
  and immersive.

- Incorporate background music into the game.

- Develop multiplayer mode and introduce player rankings.

- Add more difficulties and random events that affect the fuel and
  money.

- Implement achievements and milestones at different stages throughout
  the game.

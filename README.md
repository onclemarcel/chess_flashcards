# chess_flashcards
A quick and dirty set of flash cards on chess theory based on players experience and chess tools.\
\
Use the [authoring guide](./start.md) as a template for creating new content or just look at it to understand how to read the flash cards\
\
The purpose of this documentation is primarily a personnal work to gather information from chess books, web sites, videos, ... with the addition of Lichess statistics, screenshots & Stockfish rating to guide the reader in learning chess theory from players experience.\
\
*DISCLAIMER: I am one of the worst players in chess, but I keep being interested in capturing knowledge on this game. If this work is useful to me, why not sharing it with other people ? This is why this repository is made public, but be certain that the content may not be accurate from the reader's perspective, especially club players, amateurs, or even better ones. That said, contributions are welcome, if any, using the Github tools.*\
\
There are several ways to dive into the pages of this repository:
- Start [here](./A00_Start.md), on the first page illustrating the starting position, with links to the main first move openings
- Walk through the "code" folders to reach a specific page, especially for specific traps
- Browse [general, opening-agnostic principles](./patterns/general_principles.md) pulled from coaching commentary (currently: Daniel Naroditsky's *Speedrun: Back to 3000*, tagged `[DN-<game number>]`, e.g. `[DN-1]` for game 1)
- Browse [checkmate patterns](./mates/mate_patterns.md) — recurring mating shapes and the tactics used to force them, independent of any one opening
- Browse [irregular first moves](./A00_openings/) — Polish, Grob, Van Geet, and eleven other rare-but-playable A00 openings, one short card each
- Go straight to one of the most famous openings in the following list:

### From the initial position ###
- **White** opens with:
- [**1. e4** The King's Pawn Game](./e4_openings/B00_e4_KPG.md) to control the center, open lines for its bishop and queen, move one step to the kingside castling. One drawback is that the e4 pawn is not defended after this first move.
- **Black** may play symmetrically with :
- [**... e5**](./e4_openings/C20_e4_e5_KPG.md) to block e4 and get an equal share of the center, *but e5 becomes an undefended pawn*.
- **Black**'s single most popular reply at master level is instead asymmetrical:
- [**... c5**](./e4_openings/B20_1e4c5_Sicilian.md) the Sicilian Defense, fighting for the center on the queenside rather than matching White pawn for pawn. After 2. Nf3, Black's four main systems are the [Najdorf](./e4_openings/B50_Sicilian_d6_Open.md) (2... d6), the [Sveshnikov/Taimanov/Rossolimo family](./e4_openings/B30_Sicilian_Nc6_Open.md) (2... Nc6), the [Kan/Taimanov family](./e4_openings/B40_Sicilian_e6_Open.md) (2... e6), and the [Accelerated Dragon](./e4_openings/B34_Sicilian_g6_Accelerated_Dragon.md) (2... g6).
- **Black** may also prepare ... d5 before playing it:
- [**... e6**](./e4_openings/e4_e6_French.md) the French Defense, built out to the [Winawer/Classical](./e4_openings/e4_e6_French.md#_Nc3_) fork after 2. d4 d5 3. Nc3, or
- [**... c6**](./e4_openings/e4_c6_Caro_Kann.md) the Caro-Kann Defense, which keeps the light-squared bishop free, built out to the [Advance Variation](./e4_openings/e4_c6_Caro_Kann.md#_e5_) tabiya after 2. d4 d5 3. e5.
- **Black** may instead delay the centre entirely (hypermodern tries — rare, but sound and genuinely offbeat):
- [**... d6**](./e4_openings/B07_Pirc_Defense.md) the Pirc Defense, forking into the [Austrian Attack](./e4_openings/B08_Pirc_Defense_Tabiya.md) (4. f4) / Classical (4. Nf3) / [150 Attack](./e4_openings/B08_Pirc_Defense_Tabiya.md#_Be3_) (4. Be3) after 2. d4 Nf6 3. Nc3 g6,
- [**... g6**](./e4_openings/B06_Modern_Defense.md) the Modern (Robatsch) Defense, the same idea reached by fianchettoing first, or
- [**... Nf6**](./e4_openings/B02_Alekhine_Defense.md) the Alekhine Defense, provoking White's centre forward instead of contesting it — leads to the [Four Pawns Attack](./e4_openings/B03_Alekhine_Defense.md#_f4_) if White pushes all the way.

### From 1. e4 e5 ###
- **White** may develop its pieces with :
  - [**2. Nc3** The Vienna game](./e4_openings/C25_Nc3_Vienna_Game.md)
  - [**2. Bc4** The Bishop's Opening](./e4_openings/C23_Bc4_Bishop_Opening.md)
- **White** can play for tricks with :
  - [**2. Qh5** The Wayward Queen](./e4_openings/C20_Qh5_Wayward_Queen.md)
- **White** may attack the undefended e5 pawn with :
  - [**2. f4** The King's Gambit](./e4_openings/C30_f4_King_Gambit.md)
  - [**2. d4** The Center Game](./e4_openings/C20_d4_Center_Game.md)
  - [**2. Nf3** The King's Knight Opening](./e4_openings/C40_Nf3_King_Knight.md).

### From 1. e4 e5 2. Nf3 ###
- **Black** can the counter-attack on e4 with :
  - [**2. Nf3 f5** The Latvian Gambit](./gambits/Latvian/Latvian.md),
  - [**2. Nf3 d5** The Elephant Gambit](./gambits/Elephant/Elephant.md)
  - [**2. Nf3 Nf6** The Petrov's Defense](./e4_openings/C42_Nf3_Nf6_Petrov_Defense.md)
- **Black** can otherwise defend the e5-pawn with
  - [**2. Nf3 d6** The Philidor Defense](./e4_openings/C41_Nf3_d6_Philidor_Defense.md) 
  - [**2. Nf3 Nc6** The King's Knight Opening](./e4_openings/C44_Nf3_Nc6_King_Knight.md)

### From 1. e4 e5 2. Nf3 Nc6 ###
- **White** is able to enter into well-known openings such as:
  - [**3. Bb5**, the Spanish Opening or Ruy Lopez](./e4_openings/C60_Ruy_Lopez.md), masters' clear favourite,
  - [**3. Bc4**, the Italian Opening](./e4_openings/C50_Italian.md),
  - [**3. d4**, the Scotch Opening](./e4_openings/C44_Scotch.md),
  - [**3. Nc3**, the Four Knights Game](./e4_openings/C47_Four_Knights_Game.md).

### From the initial position, White's other first moves ###
- [**1. d4** The Queen's Pawn Game](./d4_openings/A40_d4_QPG.md), White's second most popular try (35.8% masters):
  - **1... Nf6** (60.9% masters) leads into the Indian Defense complex: [King's Indian](./d4_openings/E70_Kings_Indian.md) / [Grünfeld](./d4_openings/D85_Grunfeld.md) fork after 2. c4 g6 3. Nc3, or [Nimzo-Indian](./d4_openings/E20_Nimzo_Indian.md) / [Queen's Indian](./d4_openings/E12_Queens_Indian.md) / [Bogo-Indian](./d4_openings/E11_Bogo_Indian.md) fork after 2. c4 e6 — or, sidestepping both pin and fianchetto ideas, the [Catalan Opening](./d4_openings/E00_Catalan.md) after 2. c4 e6 3. g3. After 2. c4 c5 3. d5, Black can also gambit a pawn with the [Benko Gambit](./d4_openings/A57_Benko_Gambit.md) (3... b5, actually masters' more popular pick, 48.5%) or play the structurally committal [Modern Benoni](./d4_openings/A60_Modern_Benoni.md) (3... e6, 26.5%), and after 2. c4 e5 there's the [Budapest Gambit](./d4_openings/A51_Budapest_Gambit.md). White can also sidestep the whole complex with the [Trompowsky Attack](./d4_openings/A45_Trompowsky_Attack.md) (2. Bg5).
  - **1... d5** (25.8% masters) opens the [Queen's Gambit](./d4_openings/D06_Queens_Gambit.md) after 2. c4 (Slav 49.5% / QGD 35.3% / QGA 11.8%) — or, if White delays c4, the [Richter-Veresov Attack](./d4_openings/D01_Richter_Veresov_Attack.md) (2. Nc3) or the [Zukertort Variation](./d4_openings/D02_QPG_Nf3.md) (2. Nf3), which itself forks into the [Torre Attack](./d4_openings/D03_Torre_Attack.md), the [Colle System](./d4_openings/D04_Colle_System.md) (3. e3), and the [London System](./d4_openings/D02_London_System.md) (3. Bf4) — genuine sound-but-rarely-faced sidesteps out of mainstream Queen's Gambit/Slav theory, the London arguably the most commonly *faced* of the four despite its modest master-level share.
  - **1... f5** opens the [Dutch Defense](./d4_openings/A81_Dutch.md), built out to the Semi-Leningrad Variation.
  - **1... c5** opens the [Old Benoni](./d4_openings/A43_Old_Benoni.md) — a real surprise here: masters' own most popular reply at move 2 (2... e5, the move the line is named for) is objectively the *worst* of Black's realistic options per Stockfish.
- [**1. Nf3** The Zukertort Opening](./Nf3_openings/A04_Nf3_Zukertort.md) (10.2% masters) — flexible, most lines transpose into 1. d4 or 1. c4 territory.
- [**1. c4** The English Opening](./c4_openings/A10_c4_English.md) (6.9% masters) — a flank opening, often reached via a reversed Sicilian (1... e5) or Indian-style structures (1... Nf6), which itself transposes toward the King's Indian complex above after 2. Nc3 g6.
- [**1. b3** The Nimzo-Larsen Attack](./b3_openings/A01_Nimzo_Larsen.md) (0.4% masters) — fully sound and still a genuine top-level weapon; fianchettoes the bishop to b2 before touching the centre.
- [**1. f4** Bird's Opening](./f4_openings/A02_Bird.md) (0.2% masters) — a reversed Dutch Defense with an extra tempo, including the [From's Gambit](./f4_openings/A02_Bird.md#_e5_) trap-line for Black.

\
NOTE: all cards are linked between each other through the most common chess moves sequence that lead to the position subject of the card\
\
Special thanks to chess streamers who are spending countless hours in sharing their game experience, strategies and tactics



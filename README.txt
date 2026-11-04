Robotrek: New Bot Types v1.0

Three robot classes with different strengths, penalties and programmed
attacks, using the original Robotrek sprites and artwork

Class names appear in detailed status, the robot roster, equipment and
Program/Skill screens. The equipment label sits after the top-left rivet,
above the robot name; the programming label also follows its top-left rivet
The stat-allocation/body-color screen identifies the class above its name
The purchase selector previews the highlighted class's starting stats,
sword/gun/bomb damage multipliers and penalty
LOW GUARD means low starting Guard
GUN DELAY +1 means one extra gun recovery unit, capped at the native 12
MOVE -1 TILE means one fewer tile of battle movement


CHOOSE YOUR ROBOT

INFILTRATOR - Blue
- Best suited to melee and quick positioning
- One extra tile of movement
- Melee damage is 115% of normal
- Starts with low Guard, so protect it and invest in defense
- Guns deal 72% damage and bombs deal 75%

HUNTER - Green
- Best suited to guns and lasers
- Gun damage is 115% of normal
- Gun actions take an extra recovery unit when the gauge has room
- Gun-containing RUN programs receive that penalty once per program
- A full 12-unit recovery gauge stays at 12
- Melee and bombs both deal 82% damage

JUGGERNAUT - Red
- Starts with the most Energy and Guard
- Bomb damage is 112% of normal
- One fewer tile of movement
- Starts with low Charge, so recovery upgrades are useful
- Guns deal 75% damage and melee deals 93%

Starting stats       Energy  Power  Guard  Speed  Charge
INFILTRATOR             21      5      2      8       4
HUNTER                  21      8      4      4       3
JUGGERNAUT              24      6      7      2       1

Each class starts with 40 total points. These are permanent minimums
You can keep developing your robot and redistribute points above its floors

You can own one of each class. Owned classes are greyed out in the purchase
menu. You can highlight them to inspect their stats, but confirm does nothing
Purchase prices follow the original game:
2,000 GP for the first robot, 3,000 for the second and 4,000 for the third


RECOMMENDED EQUIPMENT

HUNTER
- Offensive setup: a gun in each arm
- Defensive setup: gun in the right arm and shield in the left
- Keep a back bomb as an optional weaker backup
- Upgrade Charge to help with gun and program recovery

INFILTRATOR
- Offensive setup: a sword in each arm
- Defensive setup: sword in the right arm and shield in the left
- Keep boots equipped and use the extra movement to position well
- Raise Energy and Guard so the melee approach is less risky

JUGGERNAUT
- Main setup: melee weapon right, shield left and bomb on the back
- Keep boots equipped to help with its shorter movement range
- Invest in Charge as well as Energy and Guard
- Use the arms as backup while making bombs the main specialty

Use the weapons available in your current chapter. These are loadout styles,
not a requirement to wait for particular late-game items. Check each arm's
power and recovery cost after changing equipment


HOW PROGRAMS WORK

R, L and X refer to equipment slots, rather than fixed weapon types:
- R uses the right arm
- L uses the left arm
- X uses the back weapon

The weapon actually equipped in a slot determines its damage family
With dual guns, both R and L use guns. With dual swords, both use melee
If you swap weapons between arms, adjust the program commands to match

At the R&D machine, choose Program, select your robot, then choose Skill
Enter the commands, confirm the program and give it a name. During battle,
choose RUN from the command menu and select your named program

The RUN list has two columns. Move right to reach the second column


RECOMMENDED PROGRAMS

HUNTER - With two guns
- RL: try one attack from each gun
- RR or LL: repeat the gun in one arm
- RRR or LLL: longer repeats only when the equipped gun costs fit
- Costly lasers may fit a two-command program but not three repeats
- With a right-arm gun and left shield, use R-based attack programs
- A normal shot can outperform a long combo against some enemies

INFILTRATOR - With two swords
- RR: a short right-arm melee combo to start with
- RRR: a longer right-arm melee combo when you can reach the target
- RL: try both swords, especially when their levels are similar
- With a left shield instead, RR and RRR still use the right sword
- Move into range before committing to a melee program

JUGGERNAUT - With a back bomb
- X: a single-bomb program and a simple starting choice
- RX: a melee-and-bomb program when the target is in melee range
- Two bomb commands cost more than the native recovery gauge allows
- Favor a single bomb when the melee part would miss

These are starting suggestions. Weapon level, enemy defense, range and
recovery all affect the result. The program screen must accept the combo
with your actual equipment before you can use it

Class bonuses and penalties also affect programmed weapon attacks
Mixed programs account for each contributing weapon's family. Native
defenses, misses, criticals and the 999 damage cap remain in effect


GAMEPLAY HINTS

- Give each robot weapons that suit its class
- Invest in Energy and Guard as well as damage
- Raise Charge to reduce time spent recovering from attacks
- Keep a shorter program available alongside a long one
- Check range before using a program that begins with melee
- Use boots and positioning to help Juggernaut reach useful positions
- Compare a program with a normal attack against the same enemy
- Switch robots when another class is better suited to the situation


INSTALL THE PATCH

- Extract Robotrek_New_Bot_Types_v1.0.zip
- Start with a clean, unheadered Robotrek (USA) ROM
- The clean ROM must be exactly 1,572,864 bytes
- Apply Robotrek_New_Bot_Types_v1.0.bps with a BPS-compatible patcher
- Apply it to the clean game each time, rather than an older patched ROM
- Save the patched game separately and open it in your emulator
- Start a new game to choose your classes normally

The ZIP contains only the BPS patch and this README.txt
A game ROM is not included


EXISTING SAVES

A new game is recommended. Back up existing saves before transferring them
R45 and newer battery saves use the same class format as this final build

R42-R44 Dark Signal saves need explicit conversion because class data has
moved. An optional conversion tool is available separately from this ZIP
Do not load an unconverted old Dark Signal save expecting its classes
to transfer automatically

Earlier builds could overwrite the third robot's skills 3-6. Conversion
resets those four skills and their names by default, so reprogram them
after loading the converted save. Data already lost in an older save
cannot be reconstructed. Other skills, stats, items and story data remain

Use a native battery save for transfer. Savestates depend on emulator and
version. Existing untyped robots display UNKNOWN and retain native behavior


TESTING

Earlier checkpoint testing covered ordinary attacks, melee/gun/bomb/mixed
RUN programs, recovery, saved classes and programs, native saving/loading,
roster ordering, Copy/Erase Log, representative status effects, KO/Repair,
native class labels, purchase previews and the ending path

Final release checks focus on choosing each class as the first purchase,
blocking owned choices, selecting the remaining third class, native saving
and cold loading of all three classes, all eight program slots and their
names on each robot, the three normal weapon families and five specialist
or mixed RUN examples, and Hunter recovery at the full 12-unit cap
The BPS patch and native ROM title are also checked independently

Testing uses representative checkpoints. A continuous full playthrough and
every possible weapon, program and stat combination remain untested

VERIFY YOUR FILES

Clean ROM SHA256
1e2ded7b1e350449b7a99b7ec414525e4b9b086c416deeee5eb3e48e032c46bd

Patched ROM SHA256
aae1caf3db48f5d2e1cea78b08efe2d3756ca1b5f8974163da1644530468c053

BPS patch SHA256
05268a257ecd00869d678017e4f9232ac48ac480acab1fb096a39b0ad61a0cda

The native ROM title is NEW BOT TYPES V1.0

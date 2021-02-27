/* Table 'game' */
CREATE TABLE game (
id serial NOT NULL,
share_code text NOT NULL,
match_time timestamp NOT NULL,
match_duration integer NOT NULL,
map_l_id serial NOT NULL,
final_score_two integer NOT NULL,
final_score_three integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player' */
CREATE TABLE player (
id serial NOT NULL,
game_id serial NOT NULL,
team_l_id integer NOT NULL,
xuid int8 NOT NULL,
user_id integer NOT NULL,
"name" text NOT NULL,
PRIMARY KEY(id));

/* Table 'map_l' */
CREATE TABLE map_l (
id integer NOT NULL,
map_name text NOT NULL,
PRIMARY KEY(id));

/* Table 'bomb_planted' */
CREATE TABLE bomb_planted (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
site integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'bomb_defused' */
CREATE TABLE bomb_defused (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
site integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_equip' */
CREATE TABLE item_equip (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
item_id integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_pickup' */
CREATE TABLE item_pickup (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
item_id integer NOT NULL,
silent bool NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_remove' */
CREATE TABLE item_remove (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
item_id integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_blind' */
CREATE TABLE player_blind (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
attacker_id serial NOT NULL,
blind_duration float4 NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_hurt' */
CREATE TABLE player_hurt (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
attacker_id serial NOT NULL,
item_id integer NOT NULL,
health integer NOT NULL,
armor integer NOT NULL,
dmg_health integer NOT NULL,
dmg_armor integer NOT NULL,
hitgroup integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_falldamage' */
CREATE TABLE player_falldamage (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
damage float4 NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_death' */
CREATE TABLE player_death (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
attacker_id serial NOT NULL,
assister_id serial NOT NULL,
item_id integer NOT NULL,
assistedflash bool NOT NULL,
headshot bool NOT NULL,
dominated bool NOT NULL,
revenge bool NOT NULL,
wipe bool NOT NULL,
penetrated bool NOT NULL,
noreplay bool NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_end' */
CREATE TABLE round_end (
id serial NOT NULL,
game_id serial NOT NULL,
team_l_id integer NOT NULL,
reason integer NOT NULL,
message text NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_mvp' */
CREATE TABLE round_mvp (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
reason integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_start' */
CREATE TABLE round_start (
id serial NOT NULL,
game_id serial NOT NULL,
timelimit integer NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'weapon_fire' */
CREATE TABLE weapon_fire (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
item_id integer NOT NULL,
silenced bool NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item' */
CREATE TABLE item (
id integer NOT NULL,
"name" text NOT NULL,
hassilencer text NOT NULL,
issilenced bool NOT NULL,
hastracers text NOT NULL,
canzoom bool NOT NULL,
item_type_l_id integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_type_l' */
CREATE TABLE item_type_l (
id integer NOT NULL,
"name" text NOT NULL,
PRIMARY KEY(id));

/* Table 'team_l' */
CREATE TABLE team_l (
id integer NOT NULL,
number integer NOT NULL,
PRIMARY KEY(id));

/* Relation 'games-players' */
ALTER TABLE player ADD CONSTRAINT "games-players"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'map_l-game' */
ALTER TABLE game ADD CONSTRAINT "map_l-game"
FOREIGN KEY (map_l_id)
REFERENCES map_l(id);

/* Relation 'player-bomb_planted' */
ALTER TABLE bomb_planted ADD CONSTRAINT "player-bomb_planted"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-bomb_defused' */
ALTER TABLE bomb_defused ADD CONSTRAINT "player-bomb_defused"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-item_equip' */
ALTER TABLE item_equip ADD CONSTRAINT "player-item_equip"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-item_pickup' */
ALTER TABLE item_pickup ADD CONSTRAINT "player-item_pickup"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-item_remove' */
ALTER TABLE item_remove ADD CONSTRAINT "player-item_remove"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-player_blind' */
ALTER TABLE player_blind ADD CONSTRAINT "player-player_blind"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'attacker-player_blind' */
ALTER TABLE player_blind ADD CONSTRAINT "attacker-player_blind"
FOREIGN KEY (attacker_id)
REFERENCES player(id);

/* Relation 'attacker-player_death' */
ALTER TABLE player_death ADD CONSTRAINT "attacker-player_death"
FOREIGN KEY (attacker_id)
REFERENCES player(id);

/* Relation 'assister-player_death' */
ALTER TABLE player_death ADD CONSTRAINT "assister-player_death"
FOREIGN KEY (assister_id)
REFERENCES player(id);

/* Relation 'player-player_hurt' */
ALTER TABLE player_hurt ADD CONSTRAINT "player-player_hurt"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'attacker-player_hurt' */
ALTER TABLE player_hurt ADD CONSTRAINT "attacker-player_hurt"
FOREIGN KEY (attacker_id)
REFERENCES player(id);

/* Relation 'player-round_mvp' */
ALTER TABLE round_mvp ADD CONSTRAINT "player-round_mvp"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'item_type_l-item' */
ALTER TABLE item ADD CONSTRAINT "item_type_l-item"
FOREIGN KEY (item_type_l_id)
REFERENCES item_type_l(id);

/* Relation 'item-item_equip' */
ALTER TABLE item_equip ADD CONSTRAINT "item-item_equip"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'item-item_pickup' */
ALTER TABLE item_pickup ADD CONSTRAINT "item-item_pickup"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'item-item_remove' */
ALTER TABLE item_remove ADD CONSTRAINT "item-item_remove"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'item-player_death' */
ALTER TABLE player_death ADD CONSTRAINT "item-player_death"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'item-player_hurt' */
ALTER TABLE player_hurt ADD CONSTRAINT "item-player_hurt"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'player-weapon_fire' */
ALTER TABLE weapon_fire ADD CONSTRAINT "player-weapon_fire"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'item-weapon_fire' */
ALTER TABLE weapon_fire ADD CONSTRAINT "item-weapon_fire"
FOREIGN KEY (item_id)
REFERENCES item(id);

/* Relation 'team_l-player' */
ALTER TABLE player ADD CONSTRAINT "team_l-player"
FOREIGN KEY (team_l_id)
REFERENCES team_l(id);

/* Relation 'team_l-round_end' */
ALTER TABLE round_end ADD CONSTRAINT "team_l-round_end"
FOREIGN KEY (team_l_id)
REFERENCES team_l(id);

/* Relation 'game-item_remove' */
ALTER TABLE item_remove ADD CONSTRAINT "game-item_remove"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-weapon_fire' */
ALTER TABLE weapon_fire ADD CONSTRAINT "game-weapon_fire"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-player_hurt' */
ALTER TABLE player_hurt ADD CONSTRAINT "game-player_hurt"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-player_death' */
ALTER TABLE player_death ADD CONSTRAINT "game-player_death"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-player_blind' */
ALTER TABLE player_blind ADD CONSTRAINT "game-player_blind"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-player_falldamage' */
ALTER TABLE player_falldamage ADD CONSTRAINT "game-player_falldamage"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-round_mvp' */
ALTER TABLE round_mvp ADD CONSTRAINT "game-round_mvp"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-bomb_planted' */
ALTER TABLE bomb_planted ADD CONSTRAINT "game-bomb_planted"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-bomb_defused' */
ALTER TABLE bomb_defused ADD CONSTRAINT "game-bomb_defused"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-item_equip' */
ALTER TABLE item_equip ADD CONSTRAINT "game-item_equip"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-item_pickup' */
ALTER TABLE item_pickup ADD CONSTRAINT "game-item_pickup"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-round_start' */
ALTER TABLE round_start ADD CONSTRAINT "game-round_start"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'game-round_end' */
ALTER TABLE round_end ADD CONSTRAINT "game-round_end"
FOREIGN KEY (game_id)
REFERENCES game(id);

/* Relation 'player-player_falldamage' */
ALTER TABLE player_falldamage ADD CONSTRAINT "player-player_falldamage"
FOREIGN KEY (player_id)
REFERENCES player(id);

/* Relation 'player-player_death' */
ALTER TABLE player_death ADD CONSTRAINT "player-player_death"
FOREIGN KEY (player_id)
REFERENCES player(id);


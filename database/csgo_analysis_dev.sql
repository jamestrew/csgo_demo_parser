COMMENT ON SCHEMA public IS 'standard public schema';

/* Table 'bomb_defused' */
CREATE TABLE public.bomb_defused (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
site integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'bomb_planted' */
CREATE TABLE public.bomb_planted (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
site integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'game' */
CREATE TABLE public.game (
id serial NOT NULL,
share_code text NOT NULL,
match_time timestamp without time zone NOT NULL,
match_duration integer NOT NULL,
map_l_id serial NOT NULL,
final_score_two integer NOT NULL,
final_score_three integer NOT NULL,
PRIMARY KEY(id),
CONSTRAINT share_code_u UNIQUE(share_code));

/* Table 'item' */
CREATE TABLE public.item (
id integer NOT NULL,
weapon_name text NOT NULL,
item_name text NOT NULL,
alternate boolean NOT NULL,
item_type_l_id integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_equip' */
CREATE TABLE public.item_equip (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
item_id integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_type_l' */
CREATE TABLE public.item_type_l (
id integer NOT NULL,
type_name text NOT NULL,
PRIMARY KEY(id));

/* Table 'map_l' */
CREATE TABLE public.map_l (
id integer NOT NULL,
map_name text NOT NULL,
PRIMARY KEY(id));

/* Table 'player' */
CREATE TABLE public.player (
id serial NOT NULL,
game_id serial NOT NULL,
team_l_id integer NOT NULL,
xuid bigint NOT NULL,
player_name text NOT NULL,
CONSTRAINT player_game UNIQUE(game_id,xuid),
PRIMARY KEY(id));

/* Table 'player_blind' */
CREATE TABLE public.player_blind (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
attacker_id serial NOT NULL,
blind_duration real NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_death' */
CREATE TABLE public.player_death (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
player_item_id integer NOT NULL,
attacker_id serial NOT NULL,
assister_id serial,
item_id integer NOT NULL,
assistedflash boolean NOT NULL,
headshot boolean NOT NULL,
dominated boolean NOT NULL,
revenge boolean NOT NULL,
wipe boolean NOT NULL,
penetrated boolean NOT NULL,
noscope boolean NOT NULL,
thrusmoke boolean NOT NULL,
attackerblind boolean NOT NULL,
distance real NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_falldamage' */
CREATE TABLE public.player_falldamage (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
damage real NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_hurt' */
CREATE TABLE public.player_hurt (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
attacker_id serial NOT NULL,
item_id integer NOT NULL,
health integer NOT NULL,
armor integer NOT NULL,
dmg_health integer NOT NULL,
dmg_armor integer NOT NULL,
hitgroup integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_end' */
CREATE TABLE public.round_end (
id serial NOT NULL,
game_id serial NOT NULL,
team_l_id integer NOT NULL,
reason integer NOT NULL,
message text NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_mvp' */
CREATE TABLE public.round_mvp (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
reason integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'round_start' */
CREATE TABLE public.round_start (
id serial NOT NULL,
game_id serial NOT NULL,
timelimit integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'team_l' */
CREATE TABLE public.team_l (
id integer NOT NULL,
number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'weapon_fire' */
CREATE TABLE public.weapon_fire (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team text NOT NULL,
item_id integer NOT NULL,
silenced boolean NOT NULL,
event_number integer NOT NULL,
PRIMARY KEY(id));

/* Table 'event_json' */
CREATE TABLE public.event_json (
id serial NOT NULL,
game_id serial NOT NULL,
"data" json NOT NULL,
PRIMARY KEY(id));

/* Relation 'game-bomb_defused' */
ALTER TABLE public.bomb_defused ADD CONSTRAINT "game-bomb_defused"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-bomb_defused' */
ALTER TABLE public.bomb_defused ADD CONSTRAINT "player-bomb_defused"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-bomb_planted' */
ALTER TABLE public.bomb_planted ADD CONSTRAINT "game-bomb_planted"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-bomb_planted' */
ALTER TABLE public.bomb_planted ADD CONSTRAINT "player-bomb_planted"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'map_l-game' */
ALTER TABLE public.game ADD CONSTRAINT "map_l-game"
FOREIGN KEY (map_l_id)
REFERENCES public.map_l(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'item_type_l-item' */
ALTER TABLE public.item ADD CONSTRAINT "item_type_l-item"
FOREIGN KEY (item_type_l_id)
REFERENCES public.item_type_l(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-item_equip' */
ALTER TABLE public.item_equip ADD CONSTRAINT "game-item_equip"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'item-item_equip' */
ALTER TABLE public.item_equip ADD CONSTRAINT "item-item_equip"
FOREIGN KEY (item_id)
REFERENCES public.item(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-item_equip' */
ALTER TABLE public.item_equip ADD CONSTRAINT "player-item_equip"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'games-players' */
ALTER TABLE public.player ADD CONSTRAINT "games-players"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'team_l-player' */
ALTER TABLE public.player ADD CONSTRAINT "team_l-player"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'attacker-player_blind' */
ALTER TABLE public.player_blind ADD CONSTRAINT "attacker-player_blind"
FOREIGN KEY (attacker_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-player_blind' */
ALTER TABLE public.player_blind ADD CONSTRAINT "game-player_blind"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-player_blind' */
ALTER TABLE public.player_blind ADD CONSTRAINT "player-player_blind"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'assister-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "assister-player_death"
FOREIGN KEY (assister_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'attacker-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "attacker-player_death"
FOREIGN KEY (attacker_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "game-player_death"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'item-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "item-player_death"
FOREIGN KEY (item_id)
REFERENCES public.item(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "player-player_death"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-player_falldamage' */
ALTER TABLE public.player_falldamage ADD CONSTRAINT "game-player_falldamage"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-player_falldamage' */
ALTER TABLE public.player_falldamage ADD CONSTRAINT "player-player_falldamage"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'attacker-player_hurt' */
ALTER TABLE public.player_hurt ADD CONSTRAINT "attacker-player_hurt"
FOREIGN KEY (attacker_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-player_hurt' */
ALTER TABLE public.player_hurt ADD CONSTRAINT "game-player_hurt"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'item-player_hurt' */
ALTER TABLE public.player_hurt ADD CONSTRAINT "item-player_hurt"
FOREIGN KEY (item_id)
REFERENCES public.item(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-player_hurt' */
ALTER TABLE public.player_hurt ADD CONSTRAINT "player-player_hurt"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-round_end' */
ALTER TABLE public.round_end ADD CONSTRAINT "game-round_end"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'team_l-round_end' */
ALTER TABLE public.round_end ADD CONSTRAINT "team_l-round_end"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-round_mvp' */
ALTER TABLE public.round_mvp ADD CONSTRAINT "game-round_mvp"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-round_mvp' */
ALTER TABLE public.round_mvp ADD CONSTRAINT "player-round_mvp"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-round_start' */
ALTER TABLE public.round_start ADD CONSTRAINT "game-round_start"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'game-weapon_fire' */
ALTER TABLE public.weapon_fire ADD CONSTRAINT "game-weapon_fire"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'item-weapon_fire' */
ALTER TABLE public.weapon_fire ADD CONSTRAINT "item-weapon_fire"
FOREIGN KEY (item_id)
REFERENCES public.item(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-weapon_fire' */
ALTER TABLE public.weapon_fire ADD CONSTRAINT "player-weapon_fire"
FOREIGN KEY (player_id)
REFERENCES public.player(id)
ON DELETE No action
ON UPDATE No action;

/* Relation 'player-item-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "player-item-player_death"
FOREIGN KEY (player_item_id)
REFERENCES public.item(id);

/* Relation 'game-event_json' */
ALTER TABLE public.event_json ADD CONSTRAINT "game-event_json"
FOREIGN KEY (game_id)
REFERENCES public.game(id);


COMMENT ON SCHEMA public IS 'standard public schema';

/* Table 'bomb_defused' */
CREATE TABLE public.bomb_defused (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
site integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'bomb_planted' */
CREATE TABLE public.bomb_planted (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
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
INSERT INTO item (id, weapon_name, item_name, alternate, item_type_l_id)
VALUES
(1, 'weapon_cz75a', 'p250', true, 1),
(2, 'weapon_deagle', 'deagle', false, 1),
(3, 'weapon_elite', 'elite', false, 1),
(4, 'weapon_fiveseven', 'fiveseven', false, 1),
(5, 'weapon_glock', 'glock', false, 1),
(6, 'weapon_hkp2000', 'hkp2000', false, 1),
(7, 'weapon_p250', 'p250', false, 1),
(8, 'weapon_revolver', 'deagle', true, 1),
(9, 'weapon_tec9', 'tec9', false, 1),
(10, 'weapon_usp_silencer', 'hkp2000', true, 1),
(11, 'weapon_mag7', 'mag7', false, 2),
(12, 'weapon_nova', 'nova', false, 2),
(13, 'weapon_sawedoff', 'sawedoff', false, 2),
(14, 'weapon_xm1014', 'xm1014', false, 2),
(15, 'weapon_m249', 'm249', false, 3),
(16, 'weapon_negev', 'negev', false, 3),
(17, 'weapon_mac10', 'mac10', false, 4),
(18, 'weapon_mp5sd', 'mp7', true, 4),
(19, 'weapon_mp7', 'mp7', false, 4),
(20, 'weapon_mp9', 'mp9', false, 4),
(21, 'weapon_p90', 'p90', false, 4),
(22, 'weapon_bizon', 'bizon', false, 4),
(23, 'weapon_ump45', 'ump45', false, 4),
(24, 'weapon_ak47', 'ak47', false, 5),
(25, 'weapon_aug', 'aug', false, 5),
(26, 'weapon_famas', 'famas', false, 5),
(27, 'weapon_galilar', 'galilar', false, 5),
(28, 'weapon_m4a1_silencer', 'm4a1', true, 5),
(29, 'weapon_m4a1', 'm4a1', false, 5),
(30, 'weapon_sg556', 'sg556', false, 5),
(31, 'weapon_awp', 'awp', false, 6),
(32, 'weapon_g3sg1', 'g3sg1', false, 6),
(33, 'weapon_scar20', 'scar20', false, 6),
(34, 'weapon_ssg08', 'ssg08', false, 6),
(35, 'weapon_taser', 'taser', false, 7),
(36, 'weapon_hegrenade', 'hegrenade', false, 8),
(37, 'weapon_flashbang', 'flashbang', false, 8),
(38, 'weapon_smokegrenade', 'smokegrenade', false, 8),
(39, 'weapon_incgrenade', 'incgrenade', false, 8),
(40, 'weapon_molotov', 'molotov', false, 8),
(41, 'weapon_decoy', 'decoy', false, 8),
(42, 'weapon_knife', 'knife', false, 7),
(43, 'weapon_knife_t', 'knife', false, 7),
(44, 'weapon_knifegg', 'knife', false, 7),
(45, 'weapon_knife_css', 'knife', false, 7),
(46, 'weapon_bayonet', 'knife', false, 7),
(47, 'weapon_knife_flip', 'knife', false, 7),
(48, 'weapon_knife_gut', 'knife', false, 7),
(49, 'weapon_knife_karambit', 'knife', false, 7),
(50, 'weapon_knife_m9_bayonet', 'knife', false, 7),
(51, 'weapon_knife_tactical', 'knife', false, 7),
(52, 'weapon_knife_butterfly', 'knife', false, 7),
(53, 'weapon_knife_falchion', 'knife', false, 7),
(54, 'weapon_knife_push', 'knife', false, 7),
(55, 'weapon_knife_survival', 'knife', false, 7),
(56, 'weapon_knife_ursus', 'knife', false, 7),
(57, 'weapon_knife_gypsy_jackknife', 'knife', false, 7),
(58, 'weapon_knife_stiletto', 'knife', false, 7),
(59, 'weapon_knife_widowmaker', 'knife', false, 7),
(60, 'weapon_knife_ghost', 'knife', false, 7),
(61, 'weapon_knife_canis', 'knife', false, 7),
(62, 'weapon_knife_cord', 'knife', false, 7),
(63, 'weapon_knife_skeleton', 'knife', false, 7),
(64, 'weapon_knife_outdoor', 'knife', false, 7),
(65, 'weapon_knife_survival_bowie', 'knife', false, 7),
(66, 'item_kevlar', 'vest', false, 0),
(67, 'item_assaultsuit', 'vesthelm', false, 0),
(68, 'item_defuser', 'defuser', false, 0),
(69, 'weapon_c4', 'c4', false, 0),
(70, 'inferno', 'inferno', false, 8);


/* Table 'item_equip' */
CREATE TABLE public.item_equip (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
item_id integer NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'item_type_l' */
CREATE TABLE public.item_type_l (
id integer NOT NULL,
type_name text NOT NULL,
PRIMARY KEY(id),
CONSTRAINT item_type_l_name UNIQUE(type_name));
INSERT INTO item_type_l (id, type_name)
VALUES
(1, 'pistol'),
(2, 'shotgun'),
(3, 'lmg'),
(4, 'smg'),
(5, 'rifle'),
(6, 'sniper'),
(7, 'melee'),
(8, 'grenade'),
(0, 'item');

/* Table 'map_l' */
CREATE TABLE public.map_l (
id integer NOT NULL,
map_name text NOT NULL,
PRIMARY KEY(id),
CONSTRAINT map_l_name UNIQUE(map_name));
INSERT INTO map_l (id, map_name)
VALUES
(1, 'de_dust2'),
(2, 'de_mirage'),
(3, 'de_inferno'),
(4, 'de_cache'),
(5, 'de_overpass'),
(6, 'de_train'),
(7, 'de_nuke'),
(8, 'de_cbble'),
(9, 'de_vertigo');


/* Table 'player' */
CREATE TABLE public.player (
id serial NOT NULL,
game_id serial NOT NULL,
first_team_l_id integer NOT NULL,
xuid text NOT NULL,
player_name text NOT NULL,
PRIMARY KEY(id));

/* Table 'player_blind' */
CREATE TABLE public.player_blind (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
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
team_l_id integer NOT NULL,
player_item_id integer NOT NULL,
attacker_id serial,
assister_id serial,
item_id integer,
assistedflash boolean NOT NULL,
headshot boolean NOT NULL,
dominated boolean NOT NULL,
revenge boolean NOT NULL,
wipe boolean NOT NULL,
penetrated boolean NOT NULL,
noscope boolean NOT NULL,
thrusmoke boolean NOT NULL,
attackerblind boolean NOT NULL,
distance real,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_falldamage' */
CREATE TABLE public.player_falldamage (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
damage real NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'player_hurt' */
CREATE TABLE public.player_hurt (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
attacker_id serial,
item_id integer,
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
team_l_id integer NOT NULL,
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

/* Table 'weapon_fire' */
CREATE TABLE public.weapon_fire (
id serial NOT NULL,
game_id serial NOT NULL,
player_id serial NOT NULL,
team_l_id integer NOT NULL,
item_id integer NOT NULL,
silenced boolean NOT NULL,
event_number integer NOT NULL,
round integer NOT NULL,
PRIMARY KEY(id));

/* Table 'event_json' */
CREATE TABLE public.event_json (
id serial NOT NULL,
game_id serial NOT NULL,
"data" json NOT NULL,
PRIMARY KEY(id));

/* Table 'team_l' */
CREATE TABLE public.team_l (
id integer NOT NULL,
team_name text NOT NULL,
PRIMARY KEY(id),
CONSTRAINT team_l_name UNIQUE(team_name));
INSERT INTO team_l (id, team_name)
VALUES
(0, 'GOTV'),
(2, 'T'),
(3, 'CT');

/* Relation 'game-bomb_defused' */
ALTER TABLE public.bomb_defused ADD CONSTRAINT "game-bomb_defused"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
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
ON DELETE Cascade
ON UPDATE No action;

/* Relation 'game-round_mvp' */
ALTER TABLE public.round_mvp ADD CONSTRAINT "game-round_mvp"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE Cascade
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
ON DELETE Cascade
ON UPDATE No action;

/* Relation 'game-weapon_fire' */
ALTER TABLE public.weapon_fire ADD CONSTRAINT "game-weapon_fire"
FOREIGN KEY (game_id)
REFERENCES public.game(id)
ON DELETE Cascade
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
REFERENCES public.game(id)
ON DELETE Cascade;

/* Relation 'game-player' */
ALTER TABLE public.player ADD CONSTRAINT "game-player"
FOREIGN KEY (game_id)
REFERENCES public.game(id);

/* Relation 'team_l-round_mvp' */
ALTER TABLE public.round_mvp ADD CONSTRAINT "team_l-round_mvp"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-player_falldamage' */
ALTER TABLE public.player_falldamage ADD CONSTRAINT "team_l-player_falldamage"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-player_blind' */
ALTER TABLE public.player_blind ADD CONSTRAINT "team_l-player_blind"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-player_hurt' */
ALTER TABLE public.player_hurt ADD CONSTRAINT "team_l-player_hurt"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-player_death' */
ALTER TABLE public.player_death ADD CONSTRAINT "team_l-player_death"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-weapon_fire' */
ALTER TABLE public.weapon_fire ADD CONSTRAINT "team_l-weapon_fire"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-item_equip' */
ALTER TABLE public.item_equip ADD CONSTRAINT "team_l-item_equip"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-bomb_planted' */
ALTER TABLE public.bomb_planted ADD CONSTRAINT "team_l-bomb_planted"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-round_end' */
ALTER TABLE public.round_end ADD CONSTRAINT "team_l-round_end"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-bomb_defused' */
ALTER TABLE public.bomb_defused ADD CONSTRAINT "team_l-bomb_defused"
FOREIGN KEY (team_l_id)
REFERENCES public.team_l(id);

/* Relation 'team_l-player' */
ALTER TABLE public.player ADD CONSTRAINT "team_l-player"
FOREIGN KEY (first_team_l_id)
REFERENCES public.team_l(id);


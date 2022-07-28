--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4 (Debian 14.4-1)
-- Dumped by pg_dump version 14.4 (Debian 14.4-1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO abdin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO abdin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO abdin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO abdin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO abdin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO abdin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authentication_intervenant; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.authentication_intervenant (
    id integer NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    email character varying(254) NOT NULL,
    first_name character varying(150) NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone,
    last_name character varying(150) NOT NULL,
    password character varying(128) NOT NULL,
    username character varying(150) NOT NULL
);


ALTER TABLE public.authentication_intervenant OWNER TO abdin;

--
-- Name: authentication_intervenant_groups; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.authentication_intervenant_groups (
    id integer NOT NULL,
    intervenant_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.authentication_intervenant_groups OWNER TO abdin;

--
-- Name: authentication_intervenant_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.authentication_intervenant_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_intervenant_groups_id_seq OWNER TO abdin;

--
-- Name: authentication_intervenant_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.authentication_intervenant_groups_id_seq OWNED BY public.authentication_intervenant_groups.id;


--
-- Name: authentication_intervenant_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.authentication_intervenant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_intervenant_id_seq OWNER TO abdin;

--
-- Name: authentication_intervenant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.authentication_intervenant_id_seq OWNED BY public.authentication_intervenant.id;


--
-- Name: authentication_intervenant_type_user; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.authentication_intervenant_type_user (
    id integer NOT NULL,
    intervenant_id integer NOT NULL,
    type_user_id integer NOT NULL
);


ALTER TABLE public.authentication_intervenant_type_user OWNER TO abdin;

--
-- Name: authentication_intervenant_type_user_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.authentication_intervenant_type_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_intervenant_type_user_id_seq OWNER TO abdin;

--
-- Name: authentication_intervenant_type_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.authentication_intervenant_type_user_id_seq OWNED BY public.authentication_intervenant_type_user.id;


--
-- Name: authentication_intervenant_user_permissions; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.authentication_intervenant_user_permissions (
    id integer NOT NULL,
    intervenant_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.authentication_intervenant_user_permissions OWNER TO abdin;

--
-- Name: authentication_intervenant_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.authentication_intervenant_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_intervenant_user_permissions_id_seq OWNER TO abdin;

--
-- Name: authentication_intervenant_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.authentication_intervenant_user_permissions_id_seq OWNED BY public.authentication_intervenant_user_permissions.id;


--
-- Name: authentication_type_user; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.authentication_type_user (
    id integer NOT NULL,
    code character varying(10) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.authentication_type_user OWNER TO abdin;

--
-- Name: authentication_type_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.authentication_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_type_id_seq OWNER TO abdin;

--
-- Name: authentication_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.authentication_type_id_seq OWNED BY public.authentication_type_user.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO abdin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO abdin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO abdin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO abdin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO abdin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: abdin
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO abdin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abdin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: abdin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO abdin;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authentication_intervenant id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant ALTER COLUMN id SET DEFAULT nextval('public.authentication_intervenant_id_seq'::regclass);


--
-- Name: authentication_intervenant_groups id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_groups ALTER COLUMN id SET DEFAULT nextval('public.authentication_intervenant_groups_id_seq'::regclass);


--
-- Name: authentication_intervenant_type_user id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_type_user ALTER COLUMN id SET DEFAULT nextval('public.authentication_intervenant_type_user_id_seq'::regclass);


--
-- Name: authentication_intervenant_user_permissions id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authentication_intervenant_user_permissions_id_seq'::regclass);


--
-- Name: authentication_type_user id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_type_user ALTER COLUMN id SET DEFAULT nextval('public.authentication_type_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_intervenant
22	Can change user	6	change_intervenant
23	Can delete user	6	delete_intervenant
24	Can view user	6	view_intervenant
25	Can add type_user	7	add_type_user
26	Can change type_user	7	change_type_user
27	Can delete type_user	7	delete_type_user
28	Can view type_user	7	view_type_user
\.


--
-- Data for Name: authentication_intervenant; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.authentication_intervenant (id, date_joined, email, first_name, is_active, is_staff, is_superuser, last_login, last_name, password, username) FROM stdin;
8	2022-07-23 16:40:56+00	de@de.de		t	f	f	2022-07-23 21:46:44.084977+00		pbkdf2_sha256$260000$hWv9Z4atHBCBfrrFaGUQzx$sIuexBBl7yvhoIZ2yBKvjY1Qk+Vz4ugkA0DigGWx3Oo=	de
1	2022-07-22 10:16:16+00			t	t	t	2022-07-23 21:55:05.292691+00		pbkdf2_sha256$260000$0MJiO6QGt2PZ3Ep1nRHj14$xzdRzh/2I0FzH8LyI2rv9UAkusegb1t3CNfHB9Niu80=	fabiskino
\.


--
-- Data for Name: authentication_intervenant_groups; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.authentication_intervenant_groups (id, intervenant_id, group_id) FROM stdin;
\.


--
-- Data for Name: authentication_intervenant_type_user; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.authentication_intervenant_type_user (id, intervenant_id, type_user_id) FROM stdin;
1	1	6
8	8	1
9	8	4
\.


--
-- Data for Name: authentication_intervenant_user_permissions; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.authentication_intervenant_user_permissions (id, intervenant_id, permission_id) FROM stdin;
\.

--
-- Data for Name: authentication_type_user; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.authentication_type_user (id, code, name) FROM stdin;
1	DE	Directeur d'Etude
2	SE	Secrétaire
3	DG	Directeur Général
4	EN	Enseignant
5	DAF	Directeur des Affaires Financières
6	AD	Admin
7	CO	Comptable
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-07-22 18:22:34.010904+00	1	Directeur d'Etude	1	[{"added": {}}]	7	1
2	2022-07-22 18:23:03.346002+00	2	Secrétaire	1	[{"added": {}}]	7	1
3	2022-07-22 18:58:14.02667+00	3	Directeur Général	1	[{"added": {}}]	7	1
4	2022-07-22 18:58:58.067233+00	4	Enseignant	1	[{"added": {}}]	7	1
5	2022-07-22 18:59:30.312089+00	5	Directeur des Affaires Financières	1	[{"added": {}}]	7	1
6	2022-07-22 18:59:48.172183+00	6	Admin	1	[{"added": {}}]	7	1
7	2022-07-22 18:59:59.675554+00	7	Comptable	1	[{"added": {}}]	7	1
8	2022-07-23 00:52:16.738281+00	1	fabiskino	2	[{"changed": {"fields": ["Type user"]}}]	6	1
9	2022-07-23 14:44:18.974327+00	2	detest	1	[{"added": {}}]	6	1
10	2022-07-23 14:45:47.575578+00	3	secretairetest	1	[{"added": {}}]	6	1
11	2022-07-23 14:46:10.752665+00	4	dgtest	1	[{"added": {}}]	6	1
12	2022-07-23 14:46:53.01134+00	5	enseignanttest	1	[{"added": {}}]	6	1
13	2022-07-23 14:47:08.573488+00	6	daftest	1	[{"added": {}}]	6	1
14	2022-07-23 14:47:35.297848+00	7	comptabletest	1	[{"added": {}}]	6	1
15	2022-07-23 16:57:51.528294+00	7	comptabletest	3		6	1
16	2022-07-23 16:57:51.557113+00	6	daftest	3		6	1
17	2022-07-23 16:57:51.568291+00	5	enseignanttest	3		6	1
18	2022-07-23 16:57:51.579231+00	4	dgtest	3		6	1
19	2022-07-23 16:57:51.590361+00	3	secretairetest	3		6	1
20	2022-07-23 16:57:51.601452+00	2	detest	3		6	1
21	2022-07-23 21:46:28.015184+00	8	de	2	[{"changed": {"fields": ["Type user"]}}]	6	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	authentication	intervenant
7	authentication	type_user
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-07-22 08:54:39.194022+00
2	authentication	0001_initial	2022-07-22 08:54:39.383387+00
3	admin	0001_initial	2022-07-22 08:54:39.48832+00
4	admin	0002_logentry_remove_auto_add	2022-07-22 08:54:39.632718+00
5	admin	0003_logentry_add_action_flag_choices	2022-07-22 08:54:39.646412+00
6	contenttypes	0002_remove_content_type_name	2022-07-22 08:54:39.716843+00
7	auth	0001_initial	2022-07-22 08:54:39.886418+00
8	auth	0002_alter_permission_name_max_length	2022-07-22 08:54:40.285033+00
9	auth	0003_alter_user_email_max_length	2022-07-22 08:54:40.319371+00
10	auth	0004_alter_user_username_opts	2022-07-22 08:54:40.342661+00
11	auth	0005_alter_user_last_login_null	2022-07-22 08:54:40.367041+00
12	auth	0006_require_contenttypes_0002	2022-07-22 08:54:40.374664+00
13	auth	0007_alter_validators_add_error_messages	2022-07-22 08:54:40.394887+00
14	auth	0008_alter_user_username_max_length	2022-07-22 08:54:40.421557+00
15	auth	0009_alter_user_last_name_max_length	2022-07-22 08:54:40.438655+00
16	auth	0010_alter_group_name_max_length	2022-07-22 08:54:40.51294+00
17	auth	0011_update_proxy_permissions	2022-07-22 08:54:40.550103+00
18	auth	0012_alter_user_first_name_max_length	2022-07-22 08:54:40.575713+00
19	authentication	0002_auto_20220720_1643	2022-07-22 08:54:40.911375+00
20	authentication	0003_auto_20220721_0955	2022-07-22 08:54:40.959351+00
21	authentication	0004_alter_intervenant_id	2022-07-22 08:54:41.198755+00
22	authentication	0005_alter_intervenant_options_alter_intervenant_managers_and_more	2022-07-22 08:54:41.545627+00
23	authentication	0006_intervenant_type	2022-07-22 08:54:42.173247+00
24	authentication	0007_auto_20220722_0852	2022-07-22 08:54:43.167118+00
25	authentication	0008_auto_20220722_0853	2022-07-22 08:54:43.348448+00
26	authentication	0009_auto_20220722_0853	2022-07-22 08:54:43.50532+00
27	sessions	0001_initial	2022-07-22 08:54:43.785099+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: abdin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
5f99njq8cm83f6zx99b3evwphk1ec66n	.eJxVjEEOwiAQRe_C2pChgBSX7j0DmYFBqgaS0q6MdzckXej2v_f-WwTctxL2zmtYkrgIJU6_G2F8ch0gPbDem4ytbutCcijyoF3eWuLX9XD_Dgr2MurMNFv0zmqPNEVlMRHM2mY_cTQEHgwYp4FUBkSLNoMzpJTKSInP4vMF8vg4QA:1oFH95:Srr_R5q0WglgoOkDbWirlMFK8e98OKaOJDeYlfrvsCc	2022-08-06 15:34:23.423245+00
roun5klfi040sju9831s2v69fx71pbou	.eJxVjEEOwiAQRe_C2pChgBSX7j0DmYFBqgaS0q6MdzckXej2v_f-WwTctxL2zmtYkrgIJU6_G2F8ch0gPbDem4ytbutCcijyoF3eWuLX9XD_Dgr2MurMNFv0zmqPNEVlMRHM2mY_cTQEHgwYp4FUBkSLNoMzpJTKSInP4vMF8vg4QA:1oFN5V:NFxAHbLe-G5DVlUoAjqAotUlojwkuub9Lt2LGdzsDrU	2022-08-06 21:55:05.302963+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 28, true);


--
-- Name: authentication_intervenant_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.authentication_intervenant_groups_id_seq', 1, false);


--
-- Name: authentication_intervenant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.authentication_intervenant_id_seq', 8, true);


--
-- Name: authentication_intervenant_type_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.authentication_intervenant_type_user_id_seq', 9, true);


--
-- Name: authentication_intervenant_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.authentication_intervenant_user_permissions_id_seq', 1, false);


--
-- Name: authentication_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.authentication_type_id_seq', 7, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 21, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 7, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abdin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 27, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authentication_intervenant_groups authentication_intervena_intervenant_id_group_id_e23571f9_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_groups
    ADD CONSTRAINT authentication_intervena_intervenant_id_group_id_e23571f9_uniq UNIQUE (intervenant_id, group_id);


--
-- Name: authentication_intervenant_user_permissions authentication_intervena_intervenant_id_permissio_a347853f_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_user_permissions
    ADD CONSTRAINT authentication_intervena_intervenant_id_permissio_a347853f_uniq UNIQUE (intervenant_id, permission_id);


--
-- Name: authentication_intervenant_type_user authentication_intervena_intervenant_id_type_user_d18fad30_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_type_user
    ADD CONSTRAINT authentication_intervena_intervenant_id_type_user_d18fad30_uniq UNIQUE (intervenant_id, type_user_id);


--
-- Name: authentication_intervenant_groups authentication_intervenant_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_groups
    ADD CONSTRAINT authentication_intervenant_groups_pkey PRIMARY KEY (id);


--
-- Name: authentication_intervenant authentication_intervenant_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant
    ADD CONSTRAINT authentication_intervenant_pkey PRIMARY KEY (id);


--
-- Name: authentication_intervenant_type_user authentication_intervenant_type_user_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_type_user
    ADD CONSTRAINT authentication_intervenant_type_user_pkey PRIMARY KEY (id);


--
-- Name: authentication_intervenant_user_permissions authentication_intervenant_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_user_permissions
    ADD CONSTRAINT authentication_intervenant_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: authentication_intervenant authentication_intervenant_username_key; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant
    ADD CONSTRAINT authentication_intervenant_username_key UNIQUE (username);


--
-- Name: authentication_type_user authentication_type_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_type_user
    ADD CONSTRAINT authentication_type_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authentication_intervenant_groups_group_id_ad5111e6; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_groups_group_id_ad5111e6 ON public.authentication_intervenant_groups USING btree (group_id);


--
-- Name: authentication_intervenant_groups_intervenant_id_870bef0c; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_groups_intervenant_id_870bef0c ON public.authentication_intervenant_groups USING btree (intervenant_id);


--
-- Name: authentication_intervenant_intervenant_id_e91e5783; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_intervenant_id_e91e5783 ON public.authentication_intervenant_user_permissions USING btree (intervenant_id);


--
-- Name: authentication_intervenant_permission_id_da838590; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_permission_id_da838590 ON public.authentication_intervenant_user_permissions USING btree (permission_id);


--
-- Name: authentication_intervenant_type_user_intervenant_id_187f0662; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_type_user_intervenant_id_187f0662 ON public.authentication_intervenant_type_user USING btree (intervenant_id);


--
-- Name: authentication_intervenant_type_user_type_user_id_f3790ddd; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_type_user_type_user_id_f3790ddd ON public.authentication_intervenant_type_user USING btree (type_user_id);


--
-- Name: authentication_intervenant_username_4f3b63cd_like; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX authentication_intervenant_username_4f3b63cd_like ON public.authentication_intervenant USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: abdin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_intervenant_groups authentication_inter_group_id_ad5111e6_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_groups
    ADD CONSTRAINT authentication_inter_group_id_ad5111e6_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_intervenant_type_user authentication_inter_intervenant_id_187f0662_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_type_user
    ADD CONSTRAINT authentication_inter_intervenant_id_187f0662_fk_authentic FOREIGN KEY (intervenant_id) REFERENCES public.authentication_intervenant(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_intervenant_user_permissions authentication_inter_permission_id_da838590_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_user_permissions
    ADD CONSTRAINT authentication_inter_permission_id_da838590_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_intervenant_type_user authentication_inter_type_user_id_f3790ddd_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.authentication_intervenant_type_user
    ADD CONSTRAINT authentication_inter_type_user_id_f3790ddd_fk_authentic FOREIGN KEY (type_user_id) REFERENCES public.authentication_type_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: abdin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.authentication_intervenant(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--


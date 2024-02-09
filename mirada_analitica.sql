PGDMP                 	        |            mirada_analitica    14.11    14.11 3    %           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            &           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            '           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            (           1262    16481    mirada_analitica    DATABASE     m   CREATE DATABASE mirada_analitica WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
     DROP DATABASE mirada_analitica;
                postgres    false            �            1259    16510 	   candidato    TABLE     Y   CREATE TABLE public.candidato (
    id_candidato integer NOT NULL,
    candidato text
);
    DROP TABLE public.candidato;
       public         heap    postgres    false            �            1259    16509    candidato_id_candidato_seq    SEQUENCE     �   CREATE SEQUENCE public.candidato_id_candidato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.candidato_id_candidato_seq;
       public          postgres    false    216            )           0    0    candidato_id_candidato_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.candidato_id_candidato_seq OWNED BY public.candidato.id_candidato;
          public          postgres    false    215            �            1259    16552    dato    TABLE     �   CREATE TABLE public.dato (
    id_dato integer NOT NULL,
    dato text,
    id_prediccion integer,
    id_estado integer,
    id_tema integer,
    id_candidato integer,
    id_red_social integer
);
    DROP TABLE public.dato;
       public         heap    postgres    false            �            1259    16551    dato_id_dato_seq    SEQUENCE     �   CREATE SEQUENCE public.dato_id_dato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.dato_id_dato_seq;
       public          postgres    false    220            *           0    0    dato_id_dato_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.dato_id_dato_seq OWNED BY public.dato.id_dato;
          public          postgres    false    219            �            1259    16492    estado    TABLE     P   CREATE TABLE public.estado (
    id_estado integer NOT NULL,
    estado text
);
    DROP TABLE public.estado;
       public         heap    postgres    false            �            1259    16491    estado_id_estado_seq    SEQUENCE     �   CREATE SEQUENCE public.estado_id_estado_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.estado_id_estado_seq;
       public          postgres    false    212            +           0    0    estado_id_estado_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.estado_id_estado_seq OWNED BY public.estado.id_estado;
          public          postgres    false    211            �            1259    16483 
   prediccion    TABLE     \   CREATE TABLE public.prediccion (
    id_prediccion integer NOT NULL,
    prediccion text
);
    DROP TABLE public.prediccion;
       public         heap    postgres    false            �            1259    16482    prediccion_id_prediccion_seq    SEQUENCE     �   CREATE SEQUENCE public.prediccion_id_prediccion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.prediccion_id_prediccion_seq;
       public          postgres    false    210            ,           0    0    prediccion_id_prediccion_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.prediccion_id_prediccion_seq OWNED BY public.prediccion.id_prediccion;
          public          postgres    false    209            �            1259    16519 
   red_social    TABLE     U   CREATE TABLE public.red_social (
    id_red integer NOT NULL,
    red_social text
);
    DROP TABLE public.red_social;
       public         heap    postgres    false            �            1259    16518    red_social_id_red_seq    SEQUENCE     �   CREATE SEQUENCE public.red_social_id_red_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.red_social_id_red_seq;
       public          postgres    false    218            -           0    0    red_social_id_red_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.red_social_id_red_seq OWNED BY public.red_social.id_red;
          public          postgres    false    217            �            1259    16501    tema    TABLE     J   CREATE TABLE public.tema (
    id_tema integer NOT NULL,
    tema text
);
    DROP TABLE public.tema;
       public         heap    postgres    false            �            1259    16500    tema_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.tema_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.tema_id_tema_seq;
       public          postgres    false    214            .           0    0    tema_id_tema_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.tema_id_tema_seq OWNED BY public.tema.id_tema;
          public          postgres    false    213            x           2604    16513    candidato id_candidato    DEFAULT     �   ALTER TABLE ONLY public.candidato ALTER COLUMN id_candidato SET DEFAULT nextval('public.candidato_id_candidato_seq'::regclass);
 E   ALTER TABLE public.candidato ALTER COLUMN id_candidato DROP DEFAULT;
       public          postgres    false    216    215    216            z           2604    16555    dato id_dato    DEFAULT     l   ALTER TABLE ONLY public.dato ALTER COLUMN id_dato SET DEFAULT nextval('public.dato_id_dato_seq'::regclass);
 ;   ALTER TABLE public.dato ALTER COLUMN id_dato DROP DEFAULT;
       public          postgres    false    220    219    220            v           2604    16495    estado id_estado    DEFAULT     t   ALTER TABLE ONLY public.estado ALTER COLUMN id_estado SET DEFAULT nextval('public.estado_id_estado_seq'::regclass);
 ?   ALTER TABLE public.estado ALTER COLUMN id_estado DROP DEFAULT;
       public          postgres    false    212    211    212            u           2604    16486    prediccion id_prediccion    DEFAULT     �   ALTER TABLE ONLY public.prediccion ALTER COLUMN id_prediccion SET DEFAULT nextval('public.prediccion_id_prediccion_seq'::regclass);
 G   ALTER TABLE public.prediccion ALTER COLUMN id_prediccion DROP DEFAULT;
       public          postgres    false    209    210    210            y           2604    16522    red_social id_red    DEFAULT     v   ALTER TABLE ONLY public.red_social ALTER COLUMN id_red SET DEFAULT nextval('public.red_social_id_red_seq'::regclass);
 @   ALTER TABLE public.red_social ALTER COLUMN id_red DROP DEFAULT;
       public          postgres    false    218    217    218            w           2604    16504    tema id_tema    DEFAULT     l   ALTER TABLE ONLY public.tema ALTER COLUMN id_tema SET DEFAULT nextval('public.tema_id_tema_seq'::regclass);
 ;   ALTER TABLE public.tema ALTER COLUMN id_tema DROP DEFAULT;
       public          postgres    false    213    214    214                      0    16510 	   candidato 
   TABLE DATA           <   COPY public.candidato (id_candidato, candidato) FROM stdin;
    public          postgres    false    216   �7       "          0    16552    dato 
   TABLE DATA           m   COPY public.dato (id_dato, dato, id_prediccion, id_estado, id_tema, id_candidato, id_red_social) FROM stdin;
    public          postgres    false    220   8                 0    16492    estado 
   TABLE DATA           3   COPY public.estado (id_estado, estado) FROM stdin;
    public          postgres    false    212   +8                 0    16483 
   prediccion 
   TABLE DATA           ?   COPY public.prediccion (id_prediccion, prediccion) FROM stdin;
    public          postgres    false    210   _9                  0    16519 
   red_social 
   TABLE DATA           8   COPY public.red_social (id_red, red_social) FROM stdin;
    public          postgres    false    218   �9                 0    16501    tema 
   TABLE DATA           -   COPY public.tema (id_tema, tema) FROM stdin;
    public          postgres    false    214   �9       /           0    0    candidato_id_candidato_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.candidato_id_candidato_seq', 3, true);
          public          postgres    false    215            0           0    0    dato_id_dato_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.dato_id_dato_seq', 1, false);
          public          postgres    false    219            1           0    0    estado_id_estado_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.estado_id_estado_seq', 33, true);
          public          postgres    false    211            2           0    0    prediccion_id_prediccion_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.prediccion_id_prediccion_seq', 2, true);
          public          postgres    false    209            3           0    0    red_social_id_red_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.red_social_id_red_seq', 2, true);
          public          postgres    false    217            4           0    0    tema_id_tema_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.tema_id_tema_seq', 3, true);
          public          postgres    false    213            �           2606    16517    candidato candidato_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.candidato
    ADD CONSTRAINT candidato_pkey PRIMARY KEY (id_candidato);
 B   ALTER TABLE ONLY public.candidato DROP CONSTRAINT candidato_pkey;
       public            postgres    false    216            �           2606    16559    dato dato_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_pkey PRIMARY KEY (id_dato);
 8   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_pkey;
       public            postgres    false    220            ~           2606    16499    estado estado_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id_estado);
 <   ALTER TABLE ONLY public.estado DROP CONSTRAINT estado_pkey;
       public            postgres    false    212            |           2606    16490    prediccion prediccion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.prediccion
    ADD CONSTRAINT prediccion_pkey PRIMARY KEY (id_prediccion);
 D   ALTER TABLE ONLY public.prediccion DROP CONSTRAINT prediccion_pkey;
       public            postgres    false    210            �           2606    16526    red_social red_social_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.red_social
    ADD CONSTRAINT red_social_pkey PRIMARY KEY (id_red);
 D   ALTER TABLE ONLY public.red_social DROP CONSTRAINT red_social_pkey;
       public            postgres    false    218            �           2606    16508    tema tema_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.tema
    ADD CONSTRAINT tema_pkey PRIMARY KEY (id_tema);
 8   ALTER TABLE ONLY public.tema DROP CONSTRAINT tema_pkey;
       public            postgres    false    214            �           2606    16575    dato dato_id_candidato_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_candidato_fkey FOREIGN KEY (id_candidato) REFERENCES public.candidato(id_candidato);
 E   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_candidato_fkey;
       public          postgres    false    220    3202    216            �           2606    16580    dato dato_id_estado_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_estado_fkey FOREIGN KEY (id_estado) REFERENCES public.estado(id_estado);
 B   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_estado_fkey;
       public          postgres    false    220    212    3198            �           2606    16560    dato dato_id_prediccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_prediccion_fkey FOREIGN KEY (id_prediccion) REFERENCES public.prediccion(id_prediccion);
 F   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_prediccion_fkey;
       public          postgres    false    220    3196    210            �           2606    16565    dato dato_id_red_social_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_red_social_fkey FOREIGN KEY (id_red_social) REFERENCES public.red_social(id_red);
 F   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_red_social_fkey;
       public          postgres    false    218    220    3204            �           2606    16570    dato dato_id_tema_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_tema_fkey FOREIGN KEY (id_tema) REFERENCES public.tema(id_tema);
 @   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_tema_fkey;
       public          postgres    false    220    3200    214               U   x�3��O��,�Qp?�0�,�J!�4��ˈ�+�(=U�pcNYbP����ʼ�*.cN��Ҕ�D����̼���\��Ģ�=... j�E      "      x������ � �         $  x�]�Kn�0D��)|�"��K7��Ȣ�O����wE-fF��@9��$�=��QR�ܤ�HW<0l�MK����d�����U�,|�0G��|���a��b�0���bP�PP��	�v�S\L9�zA�+;O���h�FsR��{�ㄴ�a(��sG��0��DK�" o�n��i�"I+�e�Qbc����C��)^������j�~�����{317C��?P�)��:�ڴF�G�1#����j�b�LWl��brAOq�׸���ՂGGO��P��GO�`�x�cHM��1�/�Ԏ^            x�3�,�/�,�,��2��KMO3c���� {�          "   x�3�tKLNM����2�,)�,)I-����� j�_         1   x�3�LKMI-J��2�L�OJ-�K,)-J�2�L�,(-IL�/����� ��     
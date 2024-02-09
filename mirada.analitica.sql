PGDMP                         |            mirada.analitica    15.5    15.5 3    1           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            2           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            3           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            4           1262    16398    mirada.analitica    DATABASE     �   CREATE DATABASE "mirada.analitica" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Mexico.1252';
 "   DROP DATABASE "mirada.analitica";
                postgres    false            �            1259    16511 	   candidato    TABLE     Y   CREATE TABLE public.candidato (
    id_candidato integer NOT NULL,
    candidato text
);
    DROP TABLE public.candidato;
       public         heap    postgres    false            �            1259    16510    candidato_id_candidato_seq    SEQUENCE     �   CREATE SEQUENCE public.candidato_id_candidato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.candidato_id_candidato_seq;
       public          postgres    false    221            5           0    0    candidato_id_candidato_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.candidato_id_candidato_seq OWNED BY public.candidato.id_candidato;
          public          postgres    false    220            �            1259    16558    dato    TABLE     �   CREATE TABLE public.dato (
    id_dato integer NOT NULL,
    dato text,
    id_prediccion integer,
    id_red_social integer,
    id_tema integer,
    id_candidato integer,
    id_estado integer
);
    DROP TABLE public.dato;
       public         heap    postgres    false            �            1259    16557    dato_id_dato_seq    SEQUENCE     �   CREATE SEQUENCE public.dato_id_dato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.dato_id_dato_seq;
       public          postgres    false    225            6           0    0    dato_id_dato_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.dato_id_dato_seq OWNED BY public.dato.id_dato;
          public          postgres    false    224            �            1259    16549    estado    TABLE     P   CREATE TABLE public.estado (
    id_estado integer NOT NULL,
    estado text
);
    DROP TABLE public.estado;
       public         heap    postgres    false            �            1259    16548    estado_id_estado_seq    SEQUENCE     �   CREATE SEQUENCE public.estado_id_estado_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.estado_id_estado_seq;
       public          postgres    false    223            7           0    0    estado_id_estado_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.estado_id_estado_seq OWNED BY public.estado.id_estado;
          public          postgres    false    222            �            1259    16400 
   prediccion    TABLE     \   CREATE TABLE public.prediccion (
    id_prediccion integer NOT NULL,
    prediccion text
);
    DROP TABLE public.prediccion;
       public         heap    postgres    false            �            1259    16399    prediccion_id_prediccion_seq    SEQUENCE     �   CREATE SEQUENCE public.prediccion_id_prediccion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.prediccion_id_prediccion_seq;
       public          postgres    false    215            8           0    0    prediccion_id_prediccion_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.prediccion_id_prediccion_seq OWNED BY public.prediccion.id_prediccion;
          public          postgres    false    214            �            1259    16478 
   red_social    TABLE     \   CREATE TABLE public.red_social (
    id_red_social integer NOT NULL,
    red_social text
);
    DROP TABLE public.red_social;
       public         heap    postgres    false            �            1259    16477    red_social_id_red_social_seq    SEQUENCE     �   CREATE SEQUENCE public.red_social_id_red_social_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.red_social_id_red_social_seq;
       public          postgres    false    219            9           0    0    red_social_id_red_social_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.red_social_id_red_social_seq OWNED BY public.red_social.id_red_social;
          public          postgres    false    218            �            1259    16409    tema    TABLE     J   CREATE TABLE public.tema (
    id_tema integer NOT NULL,
    tema text
);
    DROP TABLE public.tema;
       public         heap    postgres    false            �            1259    16408    tema_id_tema_seq    SEQUENCE     �   CREATE SEQUENCE public.tema_id_tema_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.tema_id_tema_seq;
       public          postgres    false    217            :           0    0    tema_id_tema_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.tema_id_tema_seq OWNED BY public.tema.id_tema;
          public          postgres    false    216            �           2604    16514    candidato id_candidato    DEFAULT     �   ALTER TABLE ONLY public.candidato ALTER COLUMN id_candidato SET DEFAULT nextval('public.candidato_id_candidato_seq'::regclass);
 E   ALTER TABLE public.candidato ALTER COLUMN id_candidato DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    16561    dato id_dato    DEFAULT     l   ALTER TABLE ONLY public.dato ALTER COLUMN id_dato SET DEFAULT nextval('public.dato_id_dato_seq'::regclass);
 ;   ALTER TABLE public.dato ALTER COLUMN id_dato DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    16552    estado id_estado    DEFAULT     t   ALTER TABLE ONLY public.estado ALTER COLUMN id_estado SET DEFAULT nextval('public.estado_id_estado_seq'::regclass);
 ?   ALTER TABLE public.estado ALTER COLUMN id_estado DROP DEFAULT;
       public          postgres    false    223    222    223            ~           2604    16403    prediccion id_prediccion    DEFAULT     �   ALTER TABLE ONLY public.prediccion ALTER COLUMN id_prediccion SET DEFAULT nextval('public.prediccion_id_prediccion_seq'::regclass);
 G   ALTER TABLE public.prediccion ALTER COLUMN id_prediccion DROP DEFAULT;
       public          postgres    false    214    215    215            �           2604    16481    red_social id_red_social    DEFAULT     �   ALTER TABLE ONLY public.red_social ALTER COLUMN id_red_social SET DEFAULT nextval('public.red_social_id_red_social_seq'::regclass);
 G   ALTER TABLE public.red_social ALTER COLUMN id_red_social DROP DEFAULT;
       public          postgres    false    218    219    219                       2604    16412    tema id_tema    DEFAULT     l   ALTER TABLE ONLY public.tema ALTER COLUMN id_tema SET DEFAULT nextval('public.tema_id_tema_seq'::regclass);
 ;   ALTER TABLE public.tema ALTER COLUMN id_tema DROP DEFAULT;
       public          postgres    false    217    216    217            *          0    16511 	   candidato 
   TABLE DATA           <   COPY public.candidato (id_candidato, candidato) FROM stdin;
    public          postgres    false    221   28       .          0    16558    dato 
   TABLE DATA           m   COPY public.dato (id_dato, dato, id_prediccion, id_red_social, id_tema, id_candidato, id_estado) FROM stdin;
    public          postgres    false    225   �8       ,          0    16549    estado 
   TABLE DATA           3   COPY public.estado (id_estado, estado) FROM stdin;
    public          postgres    false    223   �8       $          0    16400 
   prediccion 
   TABLE DATA           ?   COPY public.prediccion (id_prediccion, prediccion) FROM stdin;
    public          postgres    false    215   �9       (          0    16478 
   red_social 
   TABLE DATA           ?   COPY public.red_social (id_red_social, red_social) FROM stdin;
    public          postgres    false    219   :       &          0    16409    tema 
   TABLE DATA           -   COPY public.tema (id_tema, tema) FROM stdin;
    public          postgres    false    217   ,:       ;           0    0    candidato_id_candidato_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.candidato_id_candidato_seq', 3, true);
          public          postgres    false    220            <           0    0    dato_id_dato_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.dato_id_dato_seq', 1, false);
          public          postgres    false    224            =           0    0    estado_id_estado_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.estado_id_estado_seq', 33, true);
          public          postgres    false    222            >           0    0    prediccion_id_prediccion_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.prediccion_id_prediccion_seq', 2, true);
          public          postgres    false    214            ?           0    0    red_social_id_red_social_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.red_social_id_red_social_seq', 1, true);
          public          postgres    false    218            @           0    0    tema_id_tema_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.tema_id_tema_seq', 5, true);
          public          postgres    false    216            �           2606    16518    candidato candidato_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.candidato
    ADD CONSTRAINT candidato_pkey PRIMARY KEY (id_candidato);
 B   ALTER TABLE ONLY public.candidato DROP CONSTRAINT candidato_pkey;
       public            postgres    false    221            �           2606    16565    dato dato_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_pkey PRIMARY KEY (id_dato);
 8   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_pkey;
       public            postgres    false    225            �           2606    16556    estado estado_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id_estado);
 <   ALTER TABLE ONLY public.estado DROP CONSTRAINT estado_pkey;
       public            postgres    false    223            �           2606    16407    prediccion prediccion_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.prediccion
    ADD CONSTRAINT prediccion_pkey PRIMARY KEY (id_prediccion);
 D   ALTER TABLE ONLY public.prediccion DROP CONSTRAINT prediccion_pkey;
       public            postgres    false    215            �           2606    16485    red_social red_social_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.red_social
    ADD CONSTRAINT red_social_pkey PRIMARY KEY (id_red_social);
 D   ALTER TABLE ONLY public.red_social DROP CONSTRAINT red_social_pkey;
       public            postgres    false    219            �           2606    16416    tema tema_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.tema
    ADD CONSTRAINT tema_pkey PRIMARY KEY (id_tema);
 8   ALTER TABLE ONLY public.tema DROP CONSTRAINT tema_pkey;
       public            postgres    false    217            �           2606    16586    dato dato_id_candidato_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_candidato_fkey FOREIGN KEY (id_candidato) REFERENCES public.candidato(id_candidato);
 E   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_candidato_fkey;
       public          postgres    false    225    3211    221            �           2606    16566    dato dato_id_estado_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_estado_fkey FOREIGN KEY (id_estado) REFERENCES public.estado(id_estado);
 B   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_estado_fkey;
       public          postgres    false    223    3213    225            �           2606    16571    dato dato_id_prediccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_prediccion_fkey FOREIGN KEY (id_prediccion) REFERENCES public.prediccion(id_prediccion);
 F   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_prediccion_fkey;
       public          postgres    false    3205    215    225            �           2606    16576    dato dato_id_red_social_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_red_social_fkey FOREIGN KEY (id_red_social) REFERENCES public.red_social(id_red_social);
 F   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_red_social_fkey;
       public          postgres    false    219    225    3209            �           2606    16581    dato dato_id_tema_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.dato
    ADD CONSTRAINT dato_id_tema_fkey FOREIGN KEY (id_tema) REFERENCES public.tema(id_tema);
 @   ALTER TABLE ONLY public.dato DROP CONSTRAINT dato_id_tema_fkey;
       public          postgres    false    217    225    3207            *   F   x�3�L�I,M�LT(�H��KJ,��2��O��,�QHO�)K��2���/JOU ��R�r+��1z\\\ ��      .      x������ � �      ,      x�]�Kn�0D��)|�"��K7��Ȣ�O����wE-f��恎p�)JnR����%G��2�^xO�*a>P�#VT>nj��'
�O��I�E^1(�)�����Lq�M� ߕ�#c�xt4sޜ�"��Hs���ОFR�;w ����pGZb��݉-���;S�%6v�]�:$��~G����;Z�\�{��ji�n?����P���*�z�êMkd�3���#U�ZL���ԟM.�)nK�j	/ۧ�vGO)�xt��Vģ��!5	�G��d���_��79��      $      x�3�,�/�,�,��2��KMO3c���� {�      (      x�3�LKLNM�������� (?'      &   F   x�3�,(J-�LI�K�L�2�L�OJ-�K,)-J�2�L�,(-IL��2�,N�2��L9s�sR��c���� �)�     
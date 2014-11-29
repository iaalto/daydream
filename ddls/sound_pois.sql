-- Table: public.sound_pois

-- DROP TABLE public.sound_pois;

CREATE TABLE public.sound_pois
(
  sound_poi_id integer NOT NULL DEFAULT nextval('sound_pois_sound_poi_id_seq'::regclass),
  sound_poi character varying(30),
  location geography,
  content character varying(30),
  CONSTRAINT sound_pois_pk PRIMARY KEY (sound_poi_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.sound_pois
  OWNER TO daydream;

INSERT INTO public.sound_pois VALUES (
    DEFAULT,
    'Stairway to Heaven',
    ST_SetSRID(ST_Point(60.4500, 22.2667),4326)::geography,
    'stairway_to_heaven.mp3'
);


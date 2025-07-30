



CREATE TYPE decision_enum AS ENUM ('allow', 'deny');

CREATE TABLE policies (
    policy_id           SERIAL PRIMARY KEY,
    policy_name         character varying(100) NOT NULL,
    tenant              character varying(100) NOT NULL,
    subject             character varying(100) NOT NULL,
    policy_description  character varying(2048),
    action              character varying(50) NOT NULL,
    created_by          character varying(100) NOT NULL,
    policy_type         character varying(50) NOT NULL,
    policy_schema       character varying(100) NOT NULL,
    resource            JSON,
    decision            public.decision_enum,
    created             timestamp without time zone NOT NULL DEFAULT(now() at time zone'utc'),
    last_updated        timestamp without time zone NOT NULL DEFAULT(now() at time zone'utc'),
    owner               character varying(100),
    project             character varying(100),
    uuid                UUID DEFAULT gen_random_uuid()
);



ALTER SEQUENCE policies_policy_id_seq RESTART WITH 1;
CREATE UNIQUE INDEX policies_uuid_idx ON policies (uuid);
CREATE INDEX policies_tenant_subject_idx ON policies (tenant, subject);
CREATE INDEX policies_tenant_policy_type ON policies (tenant, policy_type);
CREATE INDEX policies_tenant_policy_schema ON policies (tenant, policy_schema);

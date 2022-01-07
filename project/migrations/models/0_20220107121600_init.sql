-- upgrade --
CREATE TABLE IF NOT EXISTS "lawyer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "Law_Firm_Name" VARCHAR(50) NOT NULL,
    "Law_Firm_Email_Address" VARCHAR(50) NOT NULL,
    "Loan_Range" BIGINT NOT NULL,
    "Legal_Fee" BIGINT NOT NULL,
    "Law_Firm_Priority" VARCHAR(50) NOT NULL,
    "Remarks" TEXT NOT NULL,
    "Law_Firm_Status" VARCHAR(15) NOT NULL,
    "Display_Hierarchy" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);

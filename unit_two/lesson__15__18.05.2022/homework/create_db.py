import psycopg

with psycopg.connect("dbname=test_create user=pavel password=12345;") as conn:
    with conn.cursor() as cur:

# Создаем таблицы
        cur.execute("""                
            CREATE TABLE "group" (
                "id_group" serial PRIMARY KEY,
                "name" varchar(100))
            """)
        cur.execute("""
            CREATE TABLE "student" (
                "id_student" serial PRIMARY KEY,
                "id_group" integer not null,
                "name" varchar(100))
            """)

        cur.execute("""
            CREATE TABLE "test" (
                "id_test" serial PRIMARY KEY,
                "id_student_test" integer not null,
                "theme" varchar(100),
                "tm_test" timestamp,
                "true_50" boolean)
            """)
        cur.execute("""
            CREATE TABLE "student_test" (
                "id_student" integer not null,
                "id_test" integer not null,
                "tm_create" timestamp)
            """)

#создаем констрейны
        cur.execute("""
            alter table "student" add constraint "fk_student_id_group"
            foreign key ("id_group") references "group"("id_group")
            on delete restrict;
            """)
        cur.execute("""
            alter table "student_test" add constraint "fk_student_test_id_student"
            foreign key ("id_student") references "student"("id_student")
            on delete restrict;
            """)
        cur.execute("""
            alter table "student_test" add constraint "fk_student_test_id_test"
            foreign key ("id_test") references "test"("id_test")
            on delete restrict;
            """)

        #создание индекса
        cur.execute("""
            CREATE INDEX "idx_student_id_group" ON "student" ("id_group");
            """)
        cur.execute("""
            CREATE INDEX "idx_student_test_id_student" ON "student_test" ("id_student");
            """)
        cur.execute("""
            CREATE INDEX "idx_student_test_id_test" ON "student_test" ("id_test");
            """)
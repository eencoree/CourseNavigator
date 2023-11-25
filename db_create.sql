CREATE TABLE role (
  id_role INTEGER PRIMARY KEY,
  user_role TEXT NOT NULL CHECK (user_role IN ('course_creator', 'expert', 'student'))
);

CREATE TABLE user (
  id_user INTEGER PRIMARY KEY,
  nickname VARCHAR(10) NOT NULL,
  role_id INTEGER NOT NULL,
  email VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  FOREIGN KEY (role_id) REFERENCES role (id_role)
);

CREATE TABLE course (
  id_course INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  start_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  end_date DATETIME
);

CREATE TABLE student_course (
  id_student_course INTEGER PRIMARY KEY,
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (student_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

CREATE TABLE expert_course (
  id_expert_course INTEGER PRIMARY KEY,
  expert_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (expert_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

CREATE TABLE creator_course (
  id_creator_course INTEGER PRIMARY KEY,
  course_creator_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (course_creator_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

CREATE TABLE task (
  id_task INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  type_id INTEGER,
  FOREIGN KEY (type_id) REFERENCES type (id_type)
);

CREATE TABLE status (
  id_status INTEGER PRIMARY KEY,
  status_type TEXT NOT NULL CHECK (status_type IN ('done', 'partially completed', 'not completed'))
);

CREATE TABLE type (
  id_type INTEGER PRIMARY KEY,
  task_type TEXT NOT NULL
);

CREATE TABLE step (
  id_step INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  lesson TEXT NOT NULL,
  task_id INTEGER,
  FOREIGN KEY (task_id) REFERENCES task (id_task)
);

CREATE TABLE content (
  id_content INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  student_course_id INTEGER,
  step_id INTEGER,
  FOREIGN KEY (student_course_id) REFERENCES student_course (id_student_course),
  FOREIGN KEY (step_id) REFERENCES step (id_step)
);

CREATE TABLE step_student (
  id_step_student INTEGER PRIMARY KEY,
  user_id INTEGER,
  status_id INTEGER,
  step_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id_user),
  FOREIGN KEY (status_id) REFERENCES status (id_status),
  FOREIGN KEY (step_id) REFERENCES step (id_step)
);

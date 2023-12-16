-- Create User table
CREATE TABLE user (
  id_user INTEGER PRIMARY KEY,
  nickname VARCHAR (15) NOT NULL,
  role TEXT NOT NULL,
  email VARCHAR (25) NOT NULL,
  password VARCHAR (30) NOT NULL
);

-- Create Course table
CREATE TABLE course (
  id_course INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  start_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  end_date DATETIME
);

-- Create Student_Course table
CREATE TABLE student_course (
  id_student_course INTEGER PRIMARY KEY,
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (student_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

-- Create Expert_Course table
CREATE TABLE expert_course (
  id_expert_course INTEGER PRIMARY KEY,
  expert_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (expert_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

-- Create Creator_Course table
CREATE TABLE creator_course (
  id_creator_course INTEGER PRIMARY KEY,
  course_creator_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (course_creator_id) REFERENCES user (id_user),
  FOREIGN KEY (course_id) REFERENCES course (id_course)
);

-- Create Task table
CREATE TABLE task (
  id_task INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  type_id INTEGER,
  FOREIGN KEY (type_id) REFERENCES type (id_type)
);

-- Create Type table
CREATE TABLE type (
  id_type INTEGER PRIMARY KEY,
  task_type TEXT NOT NULL
);

-- Create Step table
CREATE TABLE step (
  id_step INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  lesson TEXT NOT NULL,
  task_id INTEGER,
  FOREIGN KEY (task_id) REFERENCES task (id_task)
);

-- Create Content table
CREATE TABLE content (
  id_content INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  id_course INTEGER,
  student_course_id INTEGER,
  step_id INTEGER,
  FOREIGN KEY (id_course) REFERENCES course (id_course),
  FOREIGN KEY (student_course_id) REFERENCES student_course (id_student_course),
  FOREIGN KEY (step_id) REFERENCES step (id_step)
);

-- Create Step_Student table
CREATE TABLE step_student (
  step_student INTEGER PRIMARY KEY,
  answer TEXT,
  status TEXT,
  user_id INTEGER,
  step_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id_user),
  FOREIGN KEY (step_id) REFERENCES step (id_step)
);

-- Create AQ table
CREATE TABLE aq (
  aq_id INTEGER PRIMARY KEY,
  expert_id INTEGER,
  question TEXT NOT NULL,
  answer TEXT,
  FOREIGN KEY (expert_id) REFERENCES user (id_user)
);

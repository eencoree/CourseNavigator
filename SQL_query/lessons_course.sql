SELECT step.title, step.lesson
FROM step
JOIN content ON step.id_step = content.step_id
JOIN student_course ON content.student_course_id = student_course.id_student_course
WHERE student_course.course_id = 1;

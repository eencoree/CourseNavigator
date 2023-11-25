SELECT course.title
FROM course
JOIN expert_course ON course.id_course = expert_course.course_id
WHERE expert_course.expert_id = 1;

SELECT COUNT(DISTINCT user.id_user) AS student_count
FROM user
JOIN student_course ON user.id_user = student_course.student_id
JOIN course ON student_course.course_id = course.id_course
WHERE course.title = 'Название курса';

SELECT course.title
FROM course
JOIN student_course ON course.id_course = student_course.course_id
JOIN user ON student_course.student_id = user.id_user
WHERE user.nickname = 'ИМЯ СТУДЕНТА';

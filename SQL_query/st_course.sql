SELECT user.nickname
FROM user
JOIN student_course ON user.id_user = student_course.student_id
WHERE student_course.course_id = 1;

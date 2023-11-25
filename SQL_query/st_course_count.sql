SELECT course.title, COUNT(student_course.student_id) AS student_count
FROM course
LEFT JOIN student_course ON course.id_course = student_course.course_id
GROUP BY course.title;

-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH teacher_with_graded_assignments AS (
    SELECT teacher_id, COUNT(*) as total_graded_assignments
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
),
teacher_with_max_graded_assignments AS (
    SELECT teacher_id
    FROM teacher_with_graded_assignments
    ORDER BY total_graded_assignments DESC
    LIMIT 1
)
SELECT teacher_id, COUNT(*) FROM assignments
WHERE teacher_id = (SELECT teacher_id FROM teacher_with_max_graded_assignments) AND grade = 'A';
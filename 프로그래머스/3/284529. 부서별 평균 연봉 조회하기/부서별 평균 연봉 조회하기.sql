-- 코드를 작성해주세요
select HR_EMPLOYEES.DEPT_ID, HR_DEPARTMENT.DEPT_NAME_EN, round(avg(HR_EMPLOYEES.SAL),0) as AVG_SAL
from HR_DEPARTMENT join HR_EMPLOYEES on HR_DEPARTMENT.DEPT_ID = HR_EMPLOYEES.DEPT_ID
group by HR_EMPLOYEES.DEPT_ID
order by AVG_SAL desc


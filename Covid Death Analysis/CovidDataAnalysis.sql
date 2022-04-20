SELECT *
FROM Covid_Data..CovidDeaths
order by 3,4

--SELECT *
--FROM Covid_Data..CovidVaccination
--order by 3,4

Select Location, total_cases, new_cases, total_deaths, population
From Covid_Data..CovidDeaths
order by 1,2


-- looking case vs deaths
Select Location, total_cases, new_cases, total_deaths, death_Percentage = (total_deaths / total_cases) * 100
From Covid_Data..CovidDeaths
order by 1,2
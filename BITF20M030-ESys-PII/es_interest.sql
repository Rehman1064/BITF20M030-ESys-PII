-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: es
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `interest`
--

DROP TABLE IF EXISTS `interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interest` (
  `RollNo` int NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Dob` date DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `Interest` varchar(255) DEFAULT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `Degree` varchar(100) DEFAULT NULL,
  `Subject` varchar(100) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  PRIMARY KEY (`RollNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest` DISABLE KEYS */;
INSERT INTO `interest` VALUES (1,'John Doe','john.doe@example.com','Male','1990-01-01','City1','Interest1','Department1','Degree1','Subject1','2022-01-01','2022-12-31'),(2,'Jane Smith','jane.smith@example.com','Female','1992-05-15','City2','Data Science','Statistics','M.Sc.','Data Analysis','2022-02-01','2024-12-31'),(3,'Bob Johnson','bob.johnson@example.com','Male','1988-08-25','City3','Interest3','Department3','Degree3','Subject3','2022-03-01','2022-10-31'),(4,'Alice Williams','alice.williams@example.com','Female','1992-12-10','City4','Interest4','Department4','Degree4','Subject4','2022-04-01','2022-09-30'),(5,'Charlie Brown','charlie.brown@example.com','Male','1985-06-05','City5','Interest5','Department5','Degree5','Subject5','2022-05-01','2022-08-31'),(6,'Eva Davis','eva.davis@example.com','Female','1998-03-20','City6','Interest6','Department6','Degree6','Subject6','2022-06-01','2022-07-31'),(7,'Frank Wilson','frank.wilson@example.com','Male','1987-09-15','City7','Interest7','Department7','Degree7','Subject7','2022-07-01','2022-06-30'),(8,'Grace Miller','grace.miller@example.com','Female','1993-11-18','City8','Interest8','Department8','Degree8','Subject8','2022-08-01','2022-05-31'),(9,'David Moore','david.moore@example.com','Male','1997-02-28','City9','Interest9','Department9','Degree9','Subject9','2022-09-01','2022-04-30'),(10,'Sophie Lee','sophie.lee@example.com','Female','1989-07-12','City10','Interest10','Department10','Degree10','Subject10','2022-10-01','2022-03-31');
/*!40000 ALTER TABLE `interest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-26 23:06:09

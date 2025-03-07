-- MySQL dump 10.13  Distrib 9.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: kawiarnia_db
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `klienci`
--

DROP TABLE IF EXISTS `klienci`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `klienci` (
  `id` int NOT NULL AUTO_INCREMENT,
  `imie` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `data_rejestracji` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klienci`
--

LOCK TABLES `klienci` WRITE;
/*!40000 ALTER TABLE `klienci` DISABLE KEYS */;
INSERT INTO `klienci` VALUES (1,'Jan Kowalski','jan.kowalski@example.com','2025-02-27 21:30:14'),(2,'Anna Nowak','anna.nowak@example.com','2025-02-27 21:30:14'),(3,'Piotr Wi┼Ťniewski','piotr.wisniewski@example.com','2025-02-27 21:30:14'),(6,'Jarek Brzezina','Jeru┼Ť@wp.pl','2025-03-02 13:30:12'),(8,'Marek Wierzba','wierzba@vp.pl','2025-03-04 20:30:13');
/*!40000 ALTER TABLE `klienci` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produkty`
--

DROP TABLE IF EXISTS `produkty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produkty` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(100) NOT NULL,
  `cena` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produkty`
--

LOCK TABLES `produkty` WRITE;
/*!40000 ALTER TABLE `produkty` DISABLE KEYS */;
INSERT INTO `produkty` VALUES (1,'Espresso',10.00),(2,'Latte',12.50),(3,'Cappuccino',11.00),(4,'Herbata',8.00);
/*!40000 ALTER TABLE `produkty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `szczegoly_zamowienia`
--

DROP TABLE IF EXISTS `szczegoly_zamowienia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `szczegoly_zamowienia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `zamowienie_id` int DEFAULT NULL,
  `produkt_id` int DEFAULT NULL,
  `ilosc` int NOT NULL,
  `cena_jednostkowa` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zamowienie_id` (`zamowienie_id`),
  KEY `produkt_id` (`produkt_id`),
  CONSTRAINT `szczegoly_zamowienia_ibfk_1` FOREIGN KEY (`zamowienie_id`) REFERENCES `zamowienia` (`id`) ON DELETE CASCADE,
  CONSTRAINT `szczegoly_zamowienia_ibfk_2` FOREIGN KEY (`produkt_id`) REFERENCES `produkty` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `szczegoly_zamowienia`
--

LOCK TABLES `szczegoly_zamowienia` WRITE;
/*!40000 ALTER TABLE `szczegoly_zamowienia` DISABLE KEYS */;
INSERT INTO `szczegoly_zamowienia` VALUES (1,1,1,1,10.00),(2,1,2,1,12.50),(3,2,3,2,9.00);
/*!40000 ALTER TABLE `szczegoly_zamowienia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zamowienia`
--

DROP TABLE IF EXISTS `zamowienia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zamowienia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `klient_id` int DEFAULT NULL,
  `data_zamowienia` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `laczna_kwota` decimal(10,2) DEFAULT NULL,
  `status` enum('Nowe','W realizacji','Gotowe','Zrealizowane','Anulowane') DEFAULT 'Nowe',
  PRIMARY KEY (`id`),
  KEY `klient_id` (`klient_id`),
  CONSTRAINT `zamowienia_ibfk_1` FOREIGN KEY (`klient_id`) REFERENCES `klienci` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zamowienia`
--

LOCK TABLES `zamowienia` WRITE;
/*!40000 ALTER TABLE `zamowienia` DISABLE KEYS */;
INSERT INTO `zamowienia` VALUES (1,1,'2025-02-27 21:30:30',22.50,'W realizacji'),(2,2,'2025-02-27 21:30:30',18.00,'Zrealizowane'),(3,3,'2025-03-02 13:09:42',34.00,'Nowe'),(4,8,'2025-03-04 20:30:28',45.00,'W realizacji');
/*!40000 ALTER TABLE `zamowienia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-04 22:53:21

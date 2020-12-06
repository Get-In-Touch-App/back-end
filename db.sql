-- MariaDB dump 10.17  Distrib 10.5.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: getAholdOfMe
-- ------------------------------------------------------
-- Server version	10.5.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contactmethodflags`
--

DROP TABLE IF EXISTS `contactmethodflags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contactmethodflags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contactMethodName` varchar(255) DEFAULT NULL,
  `contactMethodFlagValue` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contactmethodflags`
--

LOCK TABLES `contactmethodflags` WRITE;
/*!40000 ALTER TABLE `contactmethodflags` DISABLE KEYS */;
INSERT INTO `contactmethodflags` VALUES (1,'email',1),(2,'text',2),(3,'voice call',4),(4,'twitter DM',8);
/*!40000 ALTER TABLE `contactmethodflags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text DEFAULT NULL,
  `sender` int(11) DEFAULT NULL,
  `receiver` int(11) DEFAULT NULL,
  `dateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Urgent !!! the cat is out of the bag',1,3,NULL),(2,'Urgent !!! the cat is out of the bag',1,2,NULL),(3,'Urgent !!! the cat is out of the bag',1,4,NULL),(4,'here\'s a message pal',1,2,NULL),(5,'here\'s another message friend',1,2,NULL),(6,'heres a message for ya',1,1,NULL),(7,'heres a message for ya',1,1,NULL),(8,'heres a message for ya',1,1,NULL),(9,'heres a message for ya',1,1,NULL),(10,'heres a message for ya',1,1,NULL),(11,'heres a message for ya',1,1,NULL),(12,'heres a message for ya',1,1,NULL),(13,'heres a message for ya',1,1,NULL),(14,'heres a message for ya',1,1,NULL),(15,'heres a message for ya',1,1,NULL),(16,'heres a message for ya pt 2',1,1,NULL),(17,'heres a message for ya pt 32',1,1,NULL),(18,'heres a message for ya pt 32',1,2,NULL),(19,'heres a message for ya pt 32',1,3,NULL),(20,'heres a message for ya pt 32',1,3,NULL),(21,'heres a message for ya pt 32',1,1,NULL),(22,'heres a message for ya pt 32',1,1,NULL),(23,'heres a message for ya pt 32',1,1,NULL),(24,'heres a message for ya pt 32',1,1,NULL),(25,'heres a message for ya pt 32',1,1,NULL),(26,'heres a message for ya pt 32',1,1,NULL),(27,'heres a message for ya pt 32',1,1,NULL),(28,'Look an email',1,1,NULL),(29,'Look an email',1,1,NULL),(30,'Look an email from a me mail',1,1,NULL),(31,'Look an email from a me mail',1,1,NULL),(32,'Look an email from a me mail',1,1,NULL),(33,'Look an email from a me mail',1,1,NULL),(34,'Look an email from a me mail',1,1,NULL),(35,'Look an email from a me mail',1,1,NULL),(36,'here\'s another message dude',1,3,NULL),(37,'here\'s another message dude',1,3,NULL),(38,'here\'s another message dude',1,1,NULL),(39,'heres a message for ya pt 32',1,1,NULL),(40,'heres a message for ya pt 32',1,1,NULL),(41,'heres a message for ya pt 32',1,1,NULL),(42,'Say No to COBOL DEVELOPMENT',1,1,NULL);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `expiration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,'XVZPOSMOVUJTJUMXIZZPIMVTYQWHWGEOTWXBOFOBCJOXEPCVNKYCAMIJCPAVGDWVPIQHJ',1,1607844139),(2,'YWVBYVTZUDIKKKDIUVPZZHYUAZCLQWPGDEVSOWGNMZVXUACBFWOJSMZXPFPJWONGUKZIL',1,1607845534),(3,'GUEPJWRTWHQTGZAJIYWSKRRTHZQGITNEKIJGQJEDNVNZPEIGWFOUKBSBZBWAVPBUYUKEZ',1,1607845573),(4,'OXNHDXHMUGBIIRDFPZZLRFZOCQRXIHWWPLQMLYJVJORPHIQQZGZMCTIAOTEWFFOSNCDVW',1,1607845597),(5,'QJMWQYRSSQUDJJITDXHDSXWUNWPVFQELIQDGUROCTAQDKLBRFGRTWIIZYENEGDFTCURCR',1,1607845599),(6,'RDXRBYJGWODGWVSRYAHWPNLBGDLLCEPURLBTWBHCHFMJAXHTDHTWENBWHBBGFCDAYAXLT',1,1607845603),(7,'NVWUUUCLJAHEYZNXBONJUEFVOZTDNSXNJAEDMYRSVCHGLLRDRFLDEHILEPVFFCYUVMEPF',1,0),(8,'MQJBWYFXZFXNFDWOCNDRTHHDBYSZOYEEKCRVJQRNZIEGHZQKYIIJAWJTZFGVVTJDOETDQ',1,1607868426),(9,'YNCFPJETJIHJXDWJEQQGTSNIDJBMUTPFBCLQXEACKQEZOCJRGOYHLQTWCHVDUEYGNBHAX',1,1607871152),(10,'ZQUCELPYFASKEULQLWZMNNREJUZVLPTFZWDWAPKCCVOCSLZBYTKCUQOEIGBTKALWSUILK',1,1607871273),(11,'SGTTOKHDRMMHQEKXAAOLMKZBTPTCMLBXRPGCYTSCZHKGLQDKVSQAALKWEYCTJFZODFEEC',1,1607875938),(12,'JMVHAPXDHSUYNSTZZYAXOBFROYEOYSRFOTVLAXFXSTRSYCCLOAABGZJXQMVPTFJSSCOKN',1,1607880896),(13,'PCZOVVKYGKKLDHNSENFOTPCJOTGBHNBDAUGZEBYXAXTDREMKDBMELQPUMZAWJDOERTDJR',1,1607882552);
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `group` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `contactMethodFlags` int(11) DEFAULT NULL,
  `twitter` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'justing','justinthegooch@gmail.com','7346869570',NULL,'SuperSecretPassword',1,''),(2,'johnSwan','johnswan@maildrop.cc','7346869570',NULL,'SuperSecretPassword',1,NULL),(3,'johnSwain','johnswain@maildrop.cc','7346869570',NULL,'SuperSecretPassword',1,NULL),(4,'michaelTrew','michaeltrew@maildrop.cc','7346869570',NULL,'SuperSecretPassword',1,NULL),(5,'joeyburgett','joeyburgett@maildrop.cc','7346869570',NULL,'SuperSecretPassword',1,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-06 13:34:22

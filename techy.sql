-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: techyroom
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-1:10.3.27+maria~focal

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add profile user',7,'add_profileuser'),(26,'Can change profile user',7,'change_profileuser'),(27,'Can delete profile user',7,'delete_profileuser'),(28,'Can view profile user',7,'view_profileuser'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add smartwatch',9,'add_smartwatch'),(34,'Can change smartwatch',9,'change_smartwatch'),(35,'Can delete smartwatch',9,'delete_smartwatch'),(36,'Can view smartwatch',9,'view_smartwatch'),(37,'Can add personal computer',10,'add_personalcomputer'),(38,'Can change personal computer',10,'change_personalcomputer'),(39,'Can delete personal computer',10,'delete_personalcomputer'),(40,'Can view personal computer',10,'view_personalcomputer'),(41,'Can add order',11,'add_order'),(42,'Can change order',11,'change_order'),(43,'Can delete order',11,'delete_order'),(44,'Can view order',11,'view_order'),(45,'Can add mouse',12,'add_mouse'),(46,'Can change mouse',12,'change_mouse'),(47,'Can delete mouse',12,'delete_mouse'),(48,'Can view mouse',12,'view_mouse'),(49,'Can add monitor',13,'add_monitor'),(50,'Can change monitor',13,'change_monitor'),(51,'Can delete monitor',13,'delete_monitor'),(52,'Can view monitor',13,'view_monitor'),(53,'Can add keyboard',14,'add_keyboard'),(54,'Can change keyboard',14,'change_keyboard'),(55,'Can delete keyboard',14,'delete_keyboard'),(56,'Can view keyboard',14,'view_keyboard'),(57,'Can add headphones',15,'add_headphones'),(58,'Can change headphones',15,'change_headphones'),(59,'Can delete headphones',15,'delete_headphones'),(60,'Can view headphones',15,'view_headphones'),(61,'Can add feedback',16,'add_feedback'),(62,'Can change feedback',16,'change_feedback'),(63,'Can delete feedback',16,'delete_feedback'),(64,'Can view feedback',16,'view_feedback'),(65,'Can add cart product',17,'add_cartproduct'),(66,'Can change cart product',17,'change_cartproduct'),(67,'Can delete cart product',17,'delete_cartproduct'),(68,'Can view cart product',17,'view_cartproduct'),(69,'Can add camera',18,'add_camera'),(70,'Can change camera',18,'change_camera'),(71,'Can delete camera',18,'delete_camera'),(72,'Can view camera',18,'view_camera'),(73,'Can add laptop',19,'add_laptop'),(74,'Can change laptop',19,'change_laptop'),(75,'Can delete laptop',19,'delete_laptop'),(76,'Can view laptop',19,'view_laptop'),(77,'Can add smartphone',20,'add_smartphone'),(78,'Can change smartphone',20,'change_smartphone'),(79,'Can delete smartphone',20,'delete_smartphone'),(80,'Can view smartphone',20,'view_smartphone');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `auth_user_email_1c89df09_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$216000$UyMeCIJXuuUY$RfqsDZJwbGkje/5ICBoe18lvXd2oFLnHDOc83I3PY5w=','2021-02-04 23:44:22.873542',1,'admin','','','aa@gmail.com',1,1,'2021-02-01 14:02:30.813122'),(4,'pbkdf2_sha256$216000$eesGxzCgtZX8$gXlk+uFdXBcndW3g3ydZ7I4MHVLfHDw0EoP0cVzy5Bc=','2021-02-04 23:44:07.347883',0,'olehtsikaylo@gmail.com','','','olehtsikaylo@gmail.com',0,1,'2021-02-03 21:49:27.256177');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-02-01 14:03:05.550124','1','Laptops',1,'[{\"added\": {}}]',8,3),(2,'2021-02-01 14:04:03.099429','1','Laptops laptop asus',1,'[{\"added\": {}}]',19,3),(3,'2021-02-01 17:15:04.508843','2','contenttype',3,'',17,3),(4,'2021-02-01 17:15:04.512274','1','contenttype',3,'',17,3),(5,'2021-02-01 19:01:26.960631','3','contenttype',3,'',17,3),(6,'2021-02-01 19:44:30.128496','2','Smartphones',1,'[{\"added\": {}}]',8,3),(7,'2021-02-01 19:46:01.789912','3','Smarphones',1,'[{\"added\": {}}]',8,3),(8,'2021-02-01 19:46:11.804958','4','wss',1,'[{\"added\": {}}]',8,3),(9,'2021-02-01 19:46:47.429963','1','10 ipx7',1,'[{\"added\": {}}]',20,3),(10,'2021-02-01 19:56:37.103776','2','Test1',3,'',11,3),(11,'2021-02-01 19:56:37.108589','1','Test1',3,'',11,3),(12,'2021-02-03 22:04:08.251216','1','Laptops laptop asus',3,'',19,3),(13,'2021-02-03 22:06:11.616995','1','10 ipx7',3,'',20,3),(14,'2021-02-03 22:07:36.966615','2','Laptops laptop asus',1,'[{\"added\": {}}]',19,3),(15,'2021-02-03 22:08:17.577078','3','Laptops op-okpokppo',1,'[{\"added\": {}}]',19,3),(16,'2021-02-03 22:17:14.097268','2','User: qerewfew Laptops sdfsdfsd',1,'[{\"added\": {}}]',7,3),(17,'2021-02-03 23:08:33.929872','2','Laptops laptop asus',3,'',19,3),(18,'2021-02-03 23:10:15.266836','11','contenttype',2,'[{\"changed\": {\"fields\": [\"ObjectId\"]}}]',17,3),(19,'2021-02-03 23:10:52.387822','11','contenttype',2,'[{\"changed\": {\"fields\": [\"ObjectId\"]}}]',17,3),(20,'2021-02-03 23:10:55.765560','8','contenttype',2,'[{\"changed\": {\"fields\": [\"ObjectId\"]}}]',17,3),(21,'2021-02-03 23:11:16.306476','11','contenttype',3,'',17,3),(22,'2021-02-03 23:11:16.308869','8','contenttype',3,'',17,3),(23,'2021-02-04 21:57:34.597231','5','Keyboards',1,'[{\"added\": {}}]',8,3),(24,'2021-02-04 21:57:55.995772','1','werwerwe werwerwe',1,'[{\"added\": {}}]',14,3),(25,'2021-02-04 21:59:02.673593','3','Laptops op-okpokppo',3,'',19,3),(26,'2021-02-04 21:59:43.252458','4','Laptops Laptop top',1,'[{\"added\": {}}]',19,3),(27,'2021-02-04 22:19:37.759973','1','werwerwe werwerwe',2,'[{\"changed\": {\"fields\": [\"Availability\"]}}]',14,3),(28,'2021-02-04 22:31:52.459295','5','Laptops laptop asus',1,'[{\"added\": {}}]',19,3),(29,'2021-02-04 22:35:08.133280','2','werwerwe werwerwe',1,'[{\"added\": {}}]',14,3),(30,'2021-02-04 22:36:02.298807','6','Laptops asus laptom super puper',1,'[{\"added\": {}}]',19,3),(31,'2021-02-04 22:46:03.308524','6','Mice',1,'[{\"added\": {}}]',8,3),(32,'2021-02-04 22:46:10.431905','1','1234',1,'[{\"added\": {}}]',12,3),(33,'2021-02-04 23:44:43.262476','6','Mice',3,'',8,3),(34,'2021-02-04 23:44:43.265212','5','Keyboards',3,'',8,3),(35,'2021-02-04 23:44:43.267255','4','wss',3,'',8,3),(36,'2021-02-04 23:44:43.268674','3','Smarphones',3,'',8,3),(37,'2021-02-04 23:44:43.270256','2','Smartphones',3,'',8,3),(38,'2021-02-04 23:44:43.271918','1','Laptops',3,'',8,3),(39,'2021-02-04 23:44:59.465728','21','admin',3,'',16,3),(40,'2021-02-04 23:44:59.469462','20','olehtsikaylo@gmail.com',3,'',16,3),(41,'2021-02-04 23:44:59.470761','19','admin',3,'',16,3),(42,'2021-02-04 23:44:59.471963','18','admin',3,'',16,3),(43,'2021-02-04 23:44:59.473118','17','admin',3,'',16,3),(44,'2021-02-04 23:44:59.474477','16','admin',3,'',16,3),(45,'2021-02-04 23:44:59.477483','15','admin',3,'',16,3),(46,'2021-02-04 23:44:59.478808','14','admin',3,'',16,3),(47,'2021-02-04 23:44:59.480015','13','admin',3,'',16,3),(48,'2021-02-04 23:44:59.481424','5','admin',3,'',16,3),(49,'2021-02-04 23:44:59.482910','4','olehtsikaylo@gmail.com',3,'',16,3),(50,'2021-02-04 23:44:59.484427','3','olehtsikaylo@gmail.com',3,'',16,3),(51,'2021-02-04 23:44:59.486942','2','olehtsikaylo@gmail.com',3,'',16,3),(52,'2021-02-04 23:44:59.489809','1','admin',3,'',16,3),(53,'2021-02-04 23:45:36.415003','30','1',3,'',11,3),(54,'2021-02-04 23:45:36.417520','29','1',3,'',11,3),(55,'2021-02-04 23:45:36.418837','28','4',3,'',11,3),(56,'2021-02-04 23:45:36.420120','27','4',3,'',11,3),(57,'2021-02-04 23:45:36.421458','26','4',3,'',11,3),(58,'2021-02-04 23:45:36.422743','25','1',3,'',11,3),(59,'2021-02-04 23:45:36.424004','24','3',3,'',11,3),(60,'2021-02-04 23:45:36.426080','23','3',3,'',11,3),(61,'2021-02-04 23:45:36.429301','22','3',3,'',11,3),(62,'2021-02-04 23:45:36.430566','21','3',3,'',11,3),(63,'2021-02-04 23:45:36.431914','20','3',3,'',11,3),(64,'2021-02-04 23:45:36.433472','19','3',3,'',11,3),(65,'2021-02-04 23:45:36.436234','18','3',3,'',11,3),(66,'2021-02-04 23:45:36.437762','17','3',3,'',11,3),(67,'2021-02-04 23:45:36.439369','16','3',3,'',11,3),(68,'2021-02-04 23:45:36.440920','15','3',3,'',11,3),(69,'2021-02-04 23:45:36.443429','14','3',3,'',11,3),(70,'2021-02-04 23:45:36.444630','13','3',3,'',11,3),(71,'2021-02-04 23:45:36.446690','12','2',3,'',11,3),(72,'2021-02-04 23:45:36.447943','11','3',3,'',11,3),(73,'2021-02-04 23:45:36.449181','10','3',3,'',11,3),(74,'2021-02-04 23:45:36.450403','9','3',3,'',11,3),(75,'2021-02-04 23:45:36.451598','8','3',3,'',11,3),(76,'2021-02-04 23:45:36.452893','7','3',3,'',11,3),(77,'2021-02-04 23:45:36.454132','6','3',3,'',11,3),(78,'2021-02-04 23:45:36.456114','5','1',3,'',11,3),(79,'2021-02-04 23:45:36.457248','4','1',3,'',11,3),(80,'2021-02-04 23:45:36.458380','3','1',3,'',11,3),(81,'2021-02-04 23:49:02.816119','7','Laptops',1,'[{\"added\": {}}]',8,3),(82,'2021-02-04 23:49:41.068878','7','Laptops laptop asus',1,'[{\"added\": {}}]',19,3),(83,'2021-02-04 23:55:06.375034','8','Laptops werewt',1,'[{\"added\": {}}]',19,3),(84,'2021-02-04 23:55:56.133774','7','Laptops',3,'',8,3),(85,'2021-02-05 10:38:08.854705','8','Laptops',1,'[{\"added\": {}}]',8,3),(86,'2021-02-05 10:41:18.353906','9','Laptops laptop asus',1,'[{\"added\": {}}]',19,3),(87,'2021-02-05 10:55:48.940264','9','Laptops laptop asus',3,'',19,3),(88,'2021-02-05 10:56:16.846456','9','Monitors',1,'[{\"added\": {}}]',8,3),(89,'2021-02-05 10:56:31.325302','10','Personal computer',1,'[{\"added\": {}}]',8,3),(90,'2021-02-05 10:56:44.987600','11','Headphones',1,'[{\"added\": {}}]',8,3),(91,'2021-02-05 10:56:57.829412','12','Keyboards',1,'[{\"added\": {}}]',8,3),(92,'2021-02-05 10:57:08.673344','13','Mice',1,'[{\"added\": {}}]',8,3),(93,'2021-02-05 10:57:31.590766','14','Smartphones',1,'[{\"added\": {}}]',8,3),(94,'2021-02-05 10:57:41.023746','15','Cameras',1,'[{\"added\": {}}]',8,3),(95,'2021-02-05 10:57:57.144981','16','Smartwatches',1,'[{\"added\": {}}]',8,3),(96,'2021-02-05 11:05:40.608799','1','MILC 24',1,'[{\"added\": {}}]',18,3),(97,'2021-02-05 11:10:27.164298','1','Over-ear 10 30000',1,'[{\"added\": {}}]',15,3),(98,'2021-02-05 11:15:25.973277','3','Mechanical Cherry MX Red',1,'[{\"added\": {}}]',14,3),(99,'2021-02-05 11:19:41.181816','10','Laptops Dell XPS 17 9700',1,'[{\"added\": {}}]',19,3),(100,'2021-02-05 11:22:34.423114','1','3840x2160',1,'[{\"added\": {}}]',13,3),(101,'2021-02-05 11:25:18.906240','2','18000',1,'[{\"added\": {}}]',12,3),(102,'2021-02-05 11:32:07.160024','1','Core i3 8100B 8',1,'[{\"added\": {}}]',10,3),(103,'2021-02-05 11:35:49.017018','1','ipx7 Plastic',1,'[{\"added\": {}}]',9,3),(104,'2021-02-05 11:40:27.735924','2','256 ipx7',1,'[{\"added\": {}}]',20,3),(105,'2021-02-05 11:41:03.902811','1','MILC 24',2,'[{\"changed\": {\"fields\": [\"Model\"]}}]',18,3),(106,'2021-02-05 11:41:11.863022','1','Over-ear 10 30000',2,'[{\"changed\": {\"fields\": [\"Model\"]}}]',15,3),(107,'2021-02-05 11:41:19.574107','3','Mechanical Cherry MX Red',2,'[{\"changed\": {\"fields\": [\"Model\"]}}]',14,3),(108,'2021-02-05 11:41:26.887964','10','Laptops XPS 17 9700',2,'[{\"changed\": {\"fields\": [\"Model\"]}}]',19,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(18,'shop','camera'),(17,'shop','cartproduct'),(8,'shop','category'),(16,'shop','feedback'),(15,'shop','headphones'),(14,'shop','keyboard'),(19,'shop','laptop'),(13,'shop','monitor'),(12,'shop','mouse'),(11,'shop','order'),(10,'shop','personalcomputer'),(20,'shop','smartphone'),(9,'shop','smartwatch'),(7,'user','profileuser');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-02-01 13:54:45.863891'),(2,'auth','0001_initial','2021-02-01 13:54:45.943823'),(3,'admin','0001_initial','2021-02-01 13:54:46.160638'),(4,'admin','0002_logentry_remove_auto_add','2021-02-01 13:54:46.216214'),(5,'admin','0003_logentry_add_action_flag_choices','2021-02-01 13:54:46.223934'),(6,'contenttypes','0002_remove_content_type_name','2021-02-01 13:54:46.272532'),(7,'auth','0002_alter_permission_name_max_length','2021-02-01 13:54:46.281583'),(8,'auth','0003_alter_user_email_max_length','2021-02-01 13:54:46.290385'),(9,'auth','0004_alter_user_username_opts','2021-02-01 13:54:46.296821'),(10,'auth','0005_alter_user_last_login_null','2021-02-01 13:54:46.332728'),(11,'auth','0006_require_contenttypes_0002','2021-02-01 13:54:46.335133'),(12,'auth','0007_alter_validators_add_error_messages','2021-02-01 13:54:46.343507'),(13,'auth','0008_alter_user_username_max_length','2021-02-01 13:54:46.353900'),(14,'auth','0009_alter_user_last_name_max_length','2021-02-01 13:54:46.363764'),(15,'auth','0010_alter_group_name_max_length','2021-02-01 13:54:46.374960'),(16,'auth','0011_update_proxy_permissions','2021-02-01 13:54:46.383217'),(17,'auth','0012_alter_user_first_name_max_length','2021-02-01 13:54:46.392243'),(18,'auth','0013_auto_20210201_1354','2021-02-01 13:54:46.405960'),(19,'sessions','0001_initial','2021-02-01 13:54:46.419375'),(20,'shop','0001_initial','2021-02-01 13:54:46.694415'),(21,'shop','0002_auto_20210127_2100','2021-02-01 13:54:47.104074'),(22,'shop','0003_auto_20210127_2109','2021-02-01 13:54:47.143724'),(23,'shop','0004_auto_20210128_1828','2021-02-01 13:54:47.477641'),(24,'shop','0005_auto_20210128_1830','2021-02-01 13:54:47.592380'),(25,'shop','0006_auto_20210201_1354','2021-02-01 13:54:47.622811'),(26,'user','0001_initial','2021-02-01 13:54:47.648680'),(27,'user','0002_auto_20210201_1354','2021-02-01 13:54:47.706008'),(28,'auth','0013_auto_20210203_2342','2021-02-03 21:47:58.066056'),(29,'shop','0006_auto_20210202_1825','2021-02-03 21:47:58.073740'),(30,'shop','0007_order_date_buy','2021-02-03 21:47:58.099743'),(31,'shop','0008_auto_20210203_2102','2021-02-03 21:47:58.268429'),(32,'user','0002_auto_20210202_1825','2021-02-03 21:47:58.279446'),(33,'shop','0009_auto_20210204_2005','2021-02-04 21:27:42.155465'),(34,'shop','0010_auto_20210205_1240','2021-02-05 10:40:49.962549');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('h3zl8cesf2yl4ug9jgio468otm8i0isx','.eJxVjMsOwiAQRf-FtSEVhse4dO83kAEGqRqalHZl_HfbpAvd3nPOfYtA61LD2nkOYxYXocXpd4uUntx2kB_U7pNMU1vmMcpdkQft8jZlfl0P9--gUq9bXSB6pRkAUTn0qDAOYF32ZDdQih4s62IVoEnpbIGx6GIcGVbgbEri8wXBbjdC:1l7oIQ:u8ZLKVVhztv-4R9uBmomMxrDfpe7BtbC2d1khO-AaLA','2021-02-18 23:44:22.877579'),('oaecvq6sz2zflxwwn30c6zgrzftk43eq','.eJxVjMsOwiAQRf-FtSEVhse4dO83kAEGqRqalHZl_HfbpAvd3nPOfYtA61LD2nkOYxYXocXpd4uUntx2kB_U7pNMU1vmMcpdkQft8jZlfl0P9--gUq9bXSB6pRkAUTn0qDAOYF32ZDdQih4s62IVoEnpbIGx6GIcGVbgbEri8wXBbjdC:1l7QFU:lg3m94VmzPOIH_8X247bpJefhbhBiw-R2N8M8ZqMjp0','2021-02-17 22:03:44.961431');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_camera`
--

DROP TABLE IF EXISTS `shop_camera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_camera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `type` varchar(128) NOT NULL,
  `matrixSize` int(10) unsigned NOT NULL CHECK (`matrixSize` >= 0),
  `megaPixels` int(10) unsigned NOT NULL CHECK (`megaPixels` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_camera_category_id_8200148a_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_camera_category_id_8200148a_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_camera`
--

LOCK TABLES `shop_camera` WRITE;
/*!40000 ALTER TABLE `shop_camera` DISABLE KEYS */;
INSERT INTO `shop_camera` VALUES (1,'EOS M50','canon-eos-m50-1612523140','Autofocus system Dual Pixel CMOS AF. 4K video recording. High rate of fire in burst mode. Rotary touch screen. A complete set of wireless communications. Compact size and light weight','products/5bdef669d724d83890f9f5df34c2d39d.jpg',26000.00,0.0,1,'Canon','China','MILC',23,24,15);
/*!40000 ALTER TABLE `shop_camera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_cartproduct`
--

DROP TABLE IF EXISTS `shop_cartproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_cartproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objectId` int(10) unsigned NOT NULL CHECK (`objectId` >= 0),
  `price` decimal(9,2) NOT NULL,
  `count` decimal(2,0) NOT NULL,
  `contentType_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_cartproduct_contentType_id_2068a60e_fk_django_co` (`contentType_id`),
  KEY `shop_cartproduct_user_id_f879de3b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_cartproduct_contentType_id_2068a60e_fk_django_co` FOREIGN KEY (`contentType_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `shop_cartproduct_user_id_f879de3b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_cartproduct`
--

LOCK TABLES `shop_cartproduct` WRITE;
/*!40000 ALTER TABLE `shop_cartproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_cartproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_category`
--

DROP TABLE IF EXISTS `shop_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_category`
--

LOCK TABLES `shop_category` WRITE;
/*!40000 ALTER TABLE `shop_category` DISABLE KEYS */;
INSERT INTO `shop_category` VALUES (8,'Laptops','laptops'),(9,'Monitors','monitors'),(10,'Personal computer','personal_computer'),(11,'Headphones','headphones'),(12,'Keyboards','keyboards'),(13,'Mice','mice'),(14,'Smartphones','smartphones'),(15,'Cameras','cameras'),(16,'Smartwatches','smartwatches');
/*!40000 ALTER TABLE `shop_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_feedback`
--

DROP TABLE IF EXISTS `shop_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `objectId` int(10) unsigned NOT NULL CHECK (`objectId` >= 0),
  `comment` longtext NOT NULL,
  `rate` int(10) unsigned NOT NULL,
  `contentType_id` int(11) NOT NULL,
  `pub_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_feedback_contentType_id_cb649eb5_fk_django_content_type_id` (`contentType_id`),
  CONSTRAINT `shop_feedback_contentType_id_cb649eb5_fk_django_content_type_id` FOREIGN KEY (`contentType_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `shop_feedback_rate_15211dd0_check` CHECK (`rate` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_feedback`
--

LOCK TABLES `shop_feedback` WRITE;
/*!40000 ALTER TABLE `shop_feedback` DISABLE KEYS */;
INSERT INTO `shop_feedback` VALUES (27,'admin',1,'Nice monitor man!',5,13,'2021-02-05');
/*!40000 ALTER TABLE `shop_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_headphones`
--

DROP TABLE IF EXISTS `shop_headphones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_headphones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `type` varchar(128) NOT NULL,
  `dynamicSize` int(10) unsigned NOT NULL CHECK (`dynamicSize` >= 0),
  `autonomyTime` int(10) unsigned NOT NULL CHECK (`autonomyTime` >= 0),
  `minFrequency` int(10) unsigned NOT NULL CHECK (`minFrequency` >= 0),
  `maxFrequency` int(10) unsigned NOT NULL CHECK (`maxFrequency` >= 0),
  `resistance` int(10) unsigned NOT NULL CHECK (`resistance` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_headphones_category_id_3970688a_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_headphones_category_id_3970688a_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_headphones`
--

LOCK TABLES `shop_headphones` WRITE;
/*!40000 ALTER TABLE `shop_headphones` DISABLE KEYS */;
INSERT INTO `shop_headphones` VALUES (1,'PX7','bw-px7-1612523427','Flagmanskaya model\' zakrytykh nakladnykh besprovodnykh naushnikov s funktsiyey aktivnogo shumopodavleniya Active Noise Cancelling (ANC), podderzhkoy kodekov aptX/ASS i vozmozhnost\'yu kabel\'nogo podklyucheniya. Otlichayutsya original\'nym firmennym dizaynom, komfortnoy posadkoy, prevoskhodnym kachestvom zvuchaniya i otlichnoy avtonomnost\'yu. Dlya organizatsii besprovodnogo podklyucheniya ispol\'zuyetsya progressivnyy energoeffektivnyy interfeys bluetooth v5.0, otlichayushchiysya uluchshennoy stabil\'nost\'yu sopryazheniy. Vstroyennyy litiy-ionnyy akkumulyator obespechivayet do 30 chasov Flagship over-ear wireless headphones with Active Noise Canceling (ANC), aptX / ACC codec support and cable connectivity. They are distinguished by their original corporate design, comfortable fit, excellent sound quality and excellent autonomy. To organize a wireless connection, a progressive energy-efficient bluetooth v5.0 interface is used, featuring improved pairing stability. Built-in lithium-ion battery provides up to 30h','products/unnamedqwe.jpg',12000.00,0.0,1,'Bowers&Wilkins','Taiwan','Over-ear',40,30,10,30000,20,11);
/*!40000 ALTER TABLE `shop_headphones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_keyboard`
--

DROP TABLE IF EXISTS `shop_keyboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_keyboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `type` varchar(128) NOT NULL,
  `switchType` varchar(128) NOT NULL,
  `autonomyTime` int(10) unsigned NOT NULL CHECK (`autonomyTime` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_keyboard_category_id_159d95ab_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_keyboard_category_id_159d95ab_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_keyboard`
--

LOCK TABLES `shop_keyboard` WRITE;
/*!40000 ALTER TABLE `shop_keyboard` DISABLE KEYS */;
INSERT INTO `shop_keyboard` VALUES (3,'Gaming K63 Compact','corsair-gaming-k63-compact-1612523725','Corsair K63 - a keyboard for those who want to enjoy maximum quality and get a reliable tool for playing and working. The model is designed as thoughtfully as possible, so the keyboard layout will not cause rejection and long habituation, but on the contrary will give a lot of pleasant sensations. The Corsair K63 is equipped with Cherry MX Red line mechanical switches, which are ideal for quick, multiple presses and have a smooth, smooth ride. The keyboard has a number of separate multimedia keys, and the firmware allows to write down a macro for any separate button and to create dynamic light effects of illumination.','products/71wyQ1uoqGL._AC_SL1500_.jpg',3000.00,0.0,1,'Corsair','China','Mechanical','Cherry MX Red',0,12);
/*!40000 ALTER TABLE `shop_keyboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_laptop`
--

DROP TABLE IF EXISTS `shop_laptop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_laptop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `diagonal` decimal(3,1) NOT NULL,
  `display` varchar(255) NOT NULL,
  `screenResolution` varchar(32) NOT NULL,
  `processor` varchar(255) NOT NULL,
  `ramType` varchar(255) NOT NULL,
  `ramSize` int(10) unsigned NOT NULL CHECK (`ramSize` >= 0),
  `videoAdapter` varchar(255) NOT NULL,
  `storageType` varchar(255) NOT NULL,
  `storageCapacity` int(10) unsigned NOT NULL CHECK (`storageCapacity` >= 0),
  `autonomyTime` int(10) unsigned NOT NULL CHECK (`autonomyTime` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_laptopproduct_category_id_0edd39cc_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_laptopproduct_category_id_0edd39cc_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_laptop`
--

LOCK TABLES `shop_laptop` WRITE;
/*!40000 ALTER TABLE `shop_laptop` DISABLE KEYS */;
INSERT INTO `shop_laptop` VALUES (10,'XPS 17 9700','dell-xps-17-9700-1612523981','A family of large-format high-performance laptops from one of the market leaders in premium portable systems. In addition to an impressively high speed, the family\'s models feature elegant carbon-fiber-reinforced aluminum housings and high-quality 17.3-inch FullHD displays with improved color gamut, light sensor and full HDR10 / Dolby Vis support.','products/2406991045.jpg',125000.00,0.0,1,'Dell','Canada',17.0,'IPS','3840x2400','Core i7 10750H','ddr4',32,'Integrated','Ssd',2048,20,8);
/*!40000 ALTER TABLE `shop_laptop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_monitor`
--

DROP TABLE IF EXISTS `shop_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_monitor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `diagonal` decimal(3,1) NOT NULL,
  `display` varchar(255) NOT NULL,
  `displayFrequency` int(10) unsigned NOT NULL CHECK (`displayFrequency` >= 0),
  `screenResolution` varchar(32) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_monitor_category_id_0cfac595_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_monitor_category_id_0cfac595_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_monitor`
--

LOCK TABLES `shop_monitor` WRITE;
/*!40000 ALTER TABLE `shop_monitor` DISABLE KEYS */;
INSERT INTO `shop_monitor` VALUES (1,'Predator XB273K','predator-xb273k-1612524154','Top gaming monitor of 2018 with a high-quality 27-inch UltraHD resolution screen, increased to 144 Hz frame rate, support for Nvidia G-Sync technology and a complete three-sided plastic screen for protection against glare. It is positioned as a premium product that can meet the demands not only of amateur gamers, but also true professionals of any e-sports discipline.','products/122894-acer-predator-xb3-2.jpg',32000.00,5.0,1,'Acer','China',27.0,'IPS',144,'3840x2160',9);
/*!40000 ALTER TABLE `shop_monitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_mouse`
--

DROP TABLE IF EXISTS `shop_mouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_mouse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `sensor` varchar(128) NOT NULL,
  `sensorDpi` int(10) unsigned NOT NULL CHECK (`sensorDpi` >= 0),
  `autonomyTime` int(10) unsigned NOT NULL CHECK (`autonomyTime` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_mouse_category_id_f054d93f_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_mouse_category_id_f054d93f_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_mouse`
--

LOCK TABLES `shop_mouse` WRITE;
/*!40000 ALTER TABLE `shop_mouse` DISABLE KEYS */;
INSERT INTO `shop_mouse` VALUES (2,'Sensei Ten','sensei-ten-1612524318','Easy-to-use gaming mouse with a symmetrical design and a set of 7 buttons, positioned by the manufacturer in the middle price segment. Made in black, has the optimal weight (96 g) and dimensions for gaming purposes. The thought-over form of the case differs in ergonomics and allows to hold a mouse with any grasp: palm, finger or claw. Optical technology with TrueMove Pro sensor provides a stable signal regardless of speed.','products/64503.jpg',2400.00,0.0,1,'SteelSeries','China','TrueMove Pro',18000,0,13);
/*!40000 ALTER TABLE `shop_mouse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_order`
--

DROP TABLE IF EXISTS `shop_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objectId` int(10) unsigned NOT NULL CHECK (`objectId` >= 0),
  `deliveryAddress` varchar(255) NOT NULL,
  `payment` varchar(255) NOT NULL,
  `contentType_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_delivery` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shop_order_contentType_id_8cb5ec66_fk_django_content_type_id` (`contentType_id`),
  KEY `shop_order_user_id_00aba627_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shop_order_contentType_id_8cb5ec66_fk_django_content_type_id` FOREIGN KEY (`contentType_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `shop_order_user_id_00aba627_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_order`
--

LOCK TABLES `shop_order` WRITE;
/*!40000 ALTER TABLE `shop_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_personalcomputer`
--

DROP TABLE IF EXISTS `shop_personalcomputer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_personalcomputer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `processor` varchar(255) NOT NULL,
  `ramType` varchar(255) NOT NULL,
  `ramSize` int(10) unsigned NOT NULL CHECK (`ramSize` >= 0),
  `videoAdapter` varchar(255) NOT NULL,
  `storageType` varchar(32) NOT NULL,
  `storageCapacity` int(10) unsigned NOT NULL CHECK (`storageCapacity` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_personalcomputer_category_id_088c3447_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_personalcomputer_category_id_088c3447_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_personalcomputer`
--

LOCK TABLES `shop_personalcomputer` WRITE;
/*!40000 ALTER TABLE `shop_personalcomputer` DISABLE KEYS */;
INSERT INTO `shop_personalcomputer` VALUES (1,'Mac mini 2018','mac-mini-2018-1612524727','Apple Mac mini Late 2018 (MRTR2) - an update to the line of compact nettops from the Cupertino giant. The device is equipped with an 8th generation Intel Core i3 processor, 8 GB of RAM and 128 GB PCI-E SSD. This is the youngest and most affordable configuration. To connect external devices, the computer received four Thunderbolt 3 ports and two USB 3.0. And in addition to the classic Gigabit Ethernet, there is dual-band WiFi 802.11ac and Bluetooth 5.0. Apple Mac mini Late 2018 (MRTR2) runs macOS Mojave. Complete with the device, the user receives only a power cable, so you need to buy additional accessories separately.','products/1821086035.jpg',17000.00,0.0,1,'Apple','USA','Core i3 8100B','ddr4',8,'Integrated','ssd',128,10);
/*!40000 ALTER TABLE `shop_personalcomputer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_smartphone`
--

DROP TABLE IF EXISTS `shop_smartphone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_smartphone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `diagonal` decimal(3,1) NOT NULL,
  `display` varchar(255) NOT NULL,
  `screenResolution` varchar(32) NOT NULL,
  `processor` varchar(255) NOT NULL,
  `ramSize` int(10) unsigned NOT NULL CHECK (`ramSize` >= 0),
  `storageCapacity` int(10) unsigned NOT NULL CHECK (`storageCapacity` >= 0),
  `moistureProtection` varchar(32) NOT NULL,
  `autonomyTime` int(10) unsigned NOT NULL CHECK (`autonomyTime` >= 0),
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_smarphone_category_id_1b42705f_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_smarphone_category_id_1b42705f_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_smartphone`
--

LOCK TABLES `shop_smartphone` WRITE;
/*!40000 ALTER TABLE `shop_smartphone` DISABLE KEYS */;
INSERT INTO `shop_smartphone` VALUES (2,'iPhone SE 2020','iphone-se-2020-1612525227','Support for wireless charging. The presence of moisture protection. Iron similar to the iPhone Xr. Emphasis on photo and video shooting. Touch ID button. Video clips recording with stereo sound (two microphones at the ends). Apple Pay support.','products/U0431068_2big_3kCES43.jpg',15000.00,0.0,1,'Apple','USA',4.7,'IPS','1334x750','Apple A13',3,256,'ipx7',30,14);
/*!40000 ALTER TABLE `shop_smartphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_smartwatch`
--

DROP TABLE IF EXISTS `shop_smartwatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop_smartwatch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(45) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `averageRate` decimal(2,1) NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `producer` varchar(64) NOT NULL,
  `producerCountry` varchar(64) NOT NULL,
  `display` varchar(255) NOT NULL,
  `moistureProtection` varchar(32) NOT NULL,
  `material` varchar(32) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `shop_smartwatch_category_id_75e1f08c_fk_shop_category_id` (`category_id`),
  CONSTRAINT `shop_smartwatch_category_id_75e1f08c_fk_shop_category_id` FOREIGN KEY (`category_id`) REFERENCES `shop_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_smartwatch`
--

LOCK TABLES `shop_smartwatch` WRITE;
/*!40000 ALTER TABLE `shop_smartwatch` DISABLE KEYS */;
INSERT INTO `shop_smartwatch` VALUES (1,'Mi Band 5','mi-band-5-1612524948','Color AMOLED display. Many options for the design of the dial. Xiao AI voice assistant. Tempered glass on top of the display. Music management on your smartphone. Detailed weather forecast. Continuous heart rate monitoring function.','products/1499826.jpeg',1500.00,0.0,1,'Xiaomi','China','AMOLED','ipx7','Plastic',16);
/*!40000 ALTER TABLE `shop_smartwatch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profileuser`
--

DROP TABLE IF EXISTS `user_profileuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profileuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(60) NOT NULL,
  `middlename` varchar(60) NOT NULL,
  `birth_date` date NOT NULL,
  `image` varchar(100) NOT NULL,
  `phone_number` varchar(128) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `user_profileuser_slug_205d57a8` (`slug`),
  KEY `user_profileuser_name_f86c0c97` (`name`),
  KEY `user_profileuser_surname_b2a0f986` (`surname`),
  KEY `user_profileuser_middlename_8e2cd043` (`middlename`),
  CONSTRAINT `user_profileuser_user_id_42574ede_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profileuser`
--

LOCK TABLES `user_profileuser` WRITE;
/*!40000 ALTER TABLE `user_profileuser` DISABLE KEYS */;
INSERT INTO `user_profileuser` VALUES (1,'user-laptopsnone','Laptops','Laptops','Laptops','1900-01-01','avatars/image_2021-01-12_15-49-16.png','+380987654321',4),(2,'user-laptopsnone','Laptops','qerewfew','sdfsdfsd','2021-02-04','avatars/photo_2021-01-12_17-00-48.jpg','+380987654321',3);
/*!40000 ALTER TABLE `user_profileuser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-05 11:55:12

CREATE DATABASE  IF NOT EXISTS `cuahangtrangsuc` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cuahangtrangsuc`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: cuahangtrangsuc
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (5,'KeToanThongKe'),(1,'NhanVienBanHang'),(2,'QuanLyCuaHang'),(3,'QuanLyKho'),(4,'QuanLyKhuyenMai'),(6,'QuanTriHeThong');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (6,1,29),(1,1,32),(2,1,46),(3,1,48),(4,1,53),(5,1,56),(7,2,25),(8,2,26),(9,2,27),(10,2,28),(11,2,29),(12,2,30),(13,2,31),(14,2,32),(15,2,33),(16,2,34),(17,2,35),(18,2,36),(19,2,37),(20,2,38),(21,2,39),(22,2,40),(23,2,41),(24,2,42),(25,2,43),(26,2,44),(27,2,45),(28,2,46),(29,2,47),(30,2,48),(31,2,49),(32,2,50),(33,2,51),(34,2,52),(35,2,53),(36,2,54),(37,2,55),(38,2,56),(39,2,57),(40,2,58),(41,2,59),(42,2,60),(43,2,61),(44,2,62),(45,2,63),(46,2,64),(47,3,49),(48,3,50),(49,3,51),(50,3,52),(51,3,56),(52,4,57),(53,4,58),(54,4,59),(55,4,60),(56,5,32),(58,5,36),(59,5,52),(57,5,56),(60,6,1),(61,6,2),(62,6,3),(63,6,4),(64,6,5),(65,6,6),(66,6,7),(67,6,8),(68,6,9),(69,6,10),(70,6,11),(71,6,12),(72,6,13),(73,6,14),(74,6,15),(75,6,16),(76,6,17),(77,6,18),(78,6,19),(79,6,20),(80,6,21),(81,6,22),(82,6,23),(83,6,24),(84,6,25),(85,6,26),(86,6,27),(87,6,28),(88,6,29),(89,6,30),(90,6,31),(91,6,32),(92,6,33),(93,6,34),(94,6,35),(95,6,36),(96,6,37),(97,6,38),(98,6,39),(99,6,40),(100,6,41),(101,6,42),(102,6,43),(103,6,44),(104,6,45),(105,6,46),(106,6,47),(107,6,48),(108,6,49),(109,6,50),(110,6,51),(111,6,52),(112,6,53),(113,6,54),(114,6,55),(115,6,56),(116,6,57),(117,6,58),(118,6,59),(119,6,60),(120,6,61),(121,6,62),(122,6,63),(123,6,64);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add gia vang',7,'add_giavang'),(26,'Can change gia vang',7,'change_giavang'),(27,'Can delete gia vang',7,'delete_giavang'),(28,'Can view gia vang',7,'view_giavang'),(29,'Can add hoa don',8,'add_hoadon'),(30,'Can change hoa don',8,'change_hoadon'),(31,'Can delete hoa don',8,'delete_hoadon'),(32,'Can view hoa don',8,'view_hoadon'),(33,'Can add khach hang',9,'add_khachhang'),(34,'Can change khach hang',9,'change_khachhang'),(35,'Can delete khach hang',9,'delete_khachhang'),(36,'Can view khach hang',9,'view_khachhang'),(37,'Can add loai san pham',10,'add_loaisanpham'),(38,'Can change loai san pham',10,'change_loaisanpham'),(39,'Can delete loai san pham',10,'delete_loaisanpham'),(40,'Can view loai san pham',10,'view_loaisanpham'),(41,'Can add nhan vien',11,'add_nhanvien'),(42,'Can change nhan vien',11,'change_nhanvien'),(43,'Can delete nhan vien',11,'delete_nhanvien'),(44,'Can view nhan vien',11,'view_nhanvien'),(45,'Can add quay ban hang',12,'add_quaybanhang'),(46,'Can change quay ban hang',12,'change_quaybanhang'),(47,'Can delete quay ban hang',12,'delete_quaybanhang'),(48,'Can view quay ban hang',12,'view_quaybanhang'),(49,'Can add san pham',13,'add_sanpham'),(50,'Can change san pham',13,'change_sanpham'),(51,'Can delete san pham',13,'delete_sanpham'),(52,'Can view san pham',13,'view_sanpham'),(53,'Can add mua lai',14,'add_mualai'),(54,'Can change mua lai',14,'change_mualai'),(55,'Can delete mua lai',14,'delete_mualai'),(56,'Can view mua lai',14,'view_mualai'),(57,'Can add khuyen mai',15,'add_khuyenmai'),(58,'Can change khuyen mai',15,'change_khuyenmai'),(59,'Can delete khuyen mai',15,'delete_khuyenmai'),(60,'Can view khuyen mai',15,'view_khuyenmai'),(61,'Can add chi tiet hoa don',16,'add_chitiethoadon'),(62,'Can change chi tiet hoa don',16,'change_chitiethoadon'),(63,'Can delete chi tiet hoa don',16,'delete_chitiethoadon'),(64,'Can view chi tiet hoa don',16,'view_chitiethoadon');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$SyBtzf1nUk4Hs2b4tEoTyn$SrhXfWl+zOw/R8RQ/V9SCu5uymCwrwsaLmyXWISKhFc=','2025-01-14 05:06:10.468513',1,'admin','','','050903tth@gmail.com',1,1,'2025-01-14 05:06:05.376985');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-01-14 05:13:43.226538','1','NhanVienBanHang',1,'[{\"added\": {}}]',3,1),(2,'2025-01-14 05:14:28.763615','2','QuanLyCuaHang',1,'[{\"added\": {}}]',3,1),(3,'2025-01-14 05:15:30.632275','3','QuanLyKho',1,'[{\"added\": {}}]',3,1),(4,'2025-01-14 05:15:52.801221','4','QuanLyKhuyenMai',1,'[{\"added\": {}}]',3,1),(5,'2025-01-14 05:16:59.694164','5','KeToanThongKe',1,'[{\"added\": {}}]',3,1),(6,'2025-01-14 05:17:15.819903','6','QuanTriHeThong',1,'[{\"added\": {}}]',3,1),(7,'2025-01-14 06:06:21.092756','123','tranthehao',1,'[{\"added\": {}}]',12,1),(8,'2025-01-14 06:06:27.379921','123','tranthehao',3,'',12,1),(9,'2025-01-14 09:30:58.210881','1','tranthehao',1,'[{\"added\": {}}]',12,1),(10,'2025-01-14 18:12:24.578123','1','tranthehao',3,'',12,1),(11,'2025-01-14 18:12:38.491972','01','Quầy số 1',1,'[{\"added\": {}}]',12,1),(12,'2025-01-14 18:12:52.136105','02','Quầy số 2',1,'[{\"added\": {}}]',12,1),(13,'2025-01-14 18:13:07.939966','03','Quầy số 3',1,'[{\"added\": {}}]',12,1),(14,'2025-01-14 18:13:17.384773','04','Quầy số 4',1,'[{\"added\": {}}]',12,1),(15,'2025-01-14 18:13:25.461491','05','Quầy số 5',1,'[{\"added\": {}}]',12,1),(16,'2025-01-14 18:31:06.518842','01','Nguyễn Văn Linh',1,'[{\"added\": {}}]',11,1),(17,'2025-01-14 18:31:23.933298','02','Trang Huyền',1,'[{\"added\": {}}]',11,1),(18,'2025-01-14 18:31:38.193129','03','Tuấn Lộc',1,'[{\"added\": {}}]',11,1),(19,'2025-01-15 04:23:09.562832','01','Quầy số 1',1,'[{\"added\": {}}]',12,1),(20,'2025-01-15 04:23:15.647508','02','Quầy số 2',1,'[{\"added\": {}}]',12,1),(21,'2025-01-15 04:23:21.618297','04','Quầy số 4',1,'[{\"added\": {}}]',12,1),(22,'2025-01-15 05:21:53.986667','01','Quầy số 1',1,'[{\"added\": {}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(16,'Quanlybanhang','chitiethoadon'),(7,'Quanlybanhang','giavang'),(8,'Quanlybanhang','hoadon'),(9,'Quanlybanhang','khachhang'),(15,'Quanlybanhang','khuyenmai'),(10,'Quanlybanhang','loaisanpham'),(14,'Quanlybanhang','mualai'),(11,'Quanlybanhang','nhanvien'),(12,'Quanlybanhang','quaybanhang'),(13,'Quanlybanhang','sanpham'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Quanlybanhang','0001_initial','2025-01-14 05:04:59.721896'),(2,'contenttypes','0001_initial','2025-01-14 05:04:59.828365'),(3,'auth','0001_initial','2025-01-14 05:05:00.642271'),(4,'admin','0001_initial','2025-01-14 05:05:00.844741'),(5,'admin','0002_logentry_remove_auto_add','2025-01-14 05:05:00.853159'),(6,'admin','0003_logentry_add_action_flag_choices','2025-01-14 05:05:00.861776'),(7,'contenttypes','0002_remove_content_type_name','2025-01-14 05:05:00.956586'),(8,'auth','0002_alter_permission_name_max_length','2025-01-14 05:05:01.029813'),(9,'auth','0003_alter_user_email_max_length','2025-01-14 05:05:01.057250'),(10,'auth','0004_alter_user_username_opts','2025-01-14 05:05:01.067731'),(11,'auth','0005_alter_user_last_login_null','2025-01-14 05:05:01.132640'),(12,'auth','0006_require_contenttypes_0002','2025-01-14 05:05:01.136567'),(13,'auth','0007_alter_validators_add_error_messages','2025-01-14 05:05:01.144032'),(14,'auth','0008_alter_user_username_max_length','2025-01-14 05:05:01.227926'),(15,'auth','0009_alter_user_last_name_max_length','2025-01-14 05:05:01.319910'),(16,'auth','0010_alter_group_name_max_length','2025-01-14 05:05:01.339776'),(17,'auth','0011_update_proxy_permissions','2025-01-14 05:05:01.353394'),(18,'auth','0012_alter_user_first_name_max_length','2025-01-14 05:05:01.436095'),(19,'sessions','0001_initial','2025-01-14 05:05:01.476196');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('oatl71nztnqo4m1bpmn3zq3b0gb1eupz','.eJxVjMEOwiAQRP-FsyGAyIJH7_0GsguLVA1NSnsy_rtt0oMeZ96beYuI61Lj2nmOYxZXocXptyNMT247yA9s90mmqS3zSHJX5EG7HKbMr9vh_h1U7HVbJ1OsYWJdABOpbB16TwbA2wDFOlMCWdQWfWDjGIO-bEnBGYwKmlh8vvIsN6Y:1tXZ7y:eJy60iPaJ_C3uvvLqN3Y3mr4-f1kyqqS7SATW1kAWEg','2025-01-28 05:06:10.472690');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_chitiethoadon`
--

DROP TABLE IF EXISTS `quanlybanhang_chitiethoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_chitiethoadon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `so_luong` int NOT NULL,
  `don_gia` decimal(10,2) NOT NULL,
  `ma_hoa_don_id` varchar(20) NOT NULL,
  `ma_san_pham_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Quanlybanhang_chitie_ma_hoa_don_id_58dfcf38_fk_Quanlyban` (`ma_hoa_don_id`),
  KEY `Quanlybanhang_chitie_ma_san_pham_id_6f145d57_fk_Quanlyban` (`ma_san_pham_id`),
  CONSTRAINT `Quanlybanhang_chitie_ma_hoa_don_id_58dfcf38_fk_Quanlyban` FOREIGN KEY (`ma_hoa_don_id`) REFERENCES `quanlybanhang_hoadon` (`ma_hoa_don`),
  CONSTRAINT `Quanlybanhang_chitie_ma_san_pham_id_6f145d57_fk_Quanlyban` FOREIGN KEY (`ma_san_pham_id`) REFERENCES `quanlybanhang_sanpham` (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_chitiethoadon`
--

LOCK TABLES `quanlybanhang_chitiethoadon` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_chitiethoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_chitiethoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_giavang`
--

DROP TABLE IF EXISTS `quanlybanhang_giavang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_giavang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `thoi_gian` datetime(6) NOT NULL,
  `gia_vang_24k` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_giavang`
--

LOCK TABLES `quanlybanhang_giavang` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_giavang` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_giavang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_hoadon`
--

DROP TABLE IF EXISTS `quanlybanhang_hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_hoadon` (
  `ma_hoa_don` varchar(20) NOT NULL,
  `ngay_lap` datetime(6) NOT NULL,
  `tong_tien` decimal(10,2) NOT NULL,
  `ma_khach_hang` varchar(20) NOT NULL,
  PRIMARY KEY (`ma_hoa_don`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_hoadon`
--

LOCK TABLES `quanlybanhang_hoadon` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_hoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_khachhang`
--

DROP TABLE IF EXISTS `quanlybanhang_khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_khachhang` (
  `ma_khach_hang` varchar(20) NOT NULL,
  `ho_ten` varchar(100) NOT NULL,
  `sdt` varchar(15) NOT NULL,
  PRIMARY KEY (`ma_khach_hang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_khachhang`
--

LOCK TABLES `quanlybanhang_khachhang` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_khachhang` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_khachhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_khuyenmai`
--

DROP TABLE IF EXISTS `quanlybanhang_khuyenmai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_khuyenmai` (
  `ma_khuyen_mai` varchar(20) NOT NULL,
  `phan_tram_chiet_khau` decimal(5,2) NOT NULL,
  `ngay_bat_dau` datetime(6) NOT NULL,
  `ngay_ket_thuc` datetime(6) NOT NULL,
  `ma_san_pham_id` varchar(20) NOT NULL,
  PRIMARY KEY (`ma_khuyen_mai`),
  KEY `Quanlybanhang_khuyen_ma_san_pham_id_6eaea86b_fk_Quanlyban` (`ma_san_pham_id`),
  CONSTRAINT `Quanlybanhang_khuyen_ma_san_pham_id_6eaea86b_fk_Quanlyban` FOREIGN KEY (`ma_san_pham_id`) REFERENCES `quanlybanhang_sanpham` (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_khuyenmai`
--

LOCK TABLES `quanlybanhang_khuyenmai` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_khuyenmai` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_khuyenmai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_loaisanpham`
--

DROP TABLE IF EXISTS `quanlybanhang_loaisanpham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_loaisanpham` (
  `ma_loai_san_pham` varchar(20) NOT NULL,
  `ten_loai_san_pham` varchar(100) NOT NULL,
  PRIMARY KEY (`ma_loai_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_loaisanpham`
--

LOCK TABLES `quanlybanhang_loaisanpham` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_loaisanpham` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_loaisanpham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_mualai`
--

DROP TABLE IF EXISTS `quanlybanhang_mualai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_mualai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngay_mua_lai` datetime(6) NOT NULL,
  `gia_mua_lai` decimal(10,2) NOT NULL,
  `ghi_chu` longtext,
  `hoa_don_id` varchar(20) NOT NULL,
  `san_pham_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Quanlybanhang_mualai_hoa_don_id_b3f7539b_fk_Quanlyban` (`hoa_don_id`),
  KEY `Quanlybanhang_mualai_san_pham_id_d1a088ae_fk_Quanlyban` (`san_pham_id`),
  CONSTRAINT `Quanlybanhang_mualai_hoa_don_id_b3f7539b_fk_Quanlyban` FOREIGN KEY (`hoa_don_id`) REFERENCES `quanlybanhang_hoadon` (`ma_hoa_don`),
  CONSTRAINT `Quanlybanhang_mualai_san_pham_id_d1a088ae_fk_Quanlyban` FOREIGN KEY (`san_pham_id`) REFERENCES `quanlybanhang_sanpham` (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_mualai`
--

LOCK TABLES `quanlybanhang_mualai` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_mualai` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_mualai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_nhanvien`
--

DROP TABLE IF EXISTS `quanlybanhang_nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_nhanvien` (
  `ma_nhan_vien` varchar(20) NOT NULL,
  `ho_ten` varchar(100) NOT NULL,
  PRIMARY KEY (`ma_nhan_vien`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_nhanvien`
--

LOCK TABLES `quanlybanhang_nhanvien` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_nhanvien` DISABLE KEYS */;
INSERT INTO `quanlybanhang_nhanvien` VALUES ('01','Nguyễn Văn Linh'),('02','Trang Huyền'),('03','Tuấn Lộc');
/*!40000 ALTER TABLE `quanlybanhang_nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_quaybanhang`
--

DROP TABLE IF EXISTS `quanlybanhang_quaybanhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_quaybanhang` (
  `ma_quay` varchar(20) NOT NULL,
  `ten_quay` varchar(100) NOT NULL,
  PRIMARY KEY (`ma_quay`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_quaybanhang`
--

LOCK TABLES `quanlybanhang_quaybanhang` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_quaybanhang` DISABLE KEYS */;
INSERT INTO `quanlybanhang_quaybanhang` VALUES ('01','Quầy số 1'),('02','Quầy số 2'),('03','Quầy số 3'),('04','Quầy số 4'),('05','Quầy số 5');
/*!40000 ALTER TABLE `quanlybanhang_quaybanhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quanlybanhang_sanpham`
--

DROP TABLE IF EXISTS `quanlybanhang_sanpham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quanlybanhang_sanpham` (
  `ma_san_pham` varchar(20) NOT NULL,
  `ten_san_pham` varchar(100) NOT NULL,
  `gia_ban` decimal(10,2) NOT NULL,
  `ton_kho` int NOT NULL,
  PRIMARY KEY (`ma_san_pham`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quanlybanhang_sanpham`
--

LOCK TABLES `quanlybanhang_sanpham` WRITE;
/*!40000 ALTER TABLE `quanlybanhang_sanpham` DISABLE KEYS */;
/*!40000 ALTER TABLE `quanlybanhang_sanpham` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-15  0:41:17

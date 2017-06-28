/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.6.24 : Database - college
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`college` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `college`;

/*Table structure for table `college_areascoreline` */

DROP TABLE IF EXISTS `college_areascoreline`;

CREATE TABLE `college_areascoreline` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DateYear` int(11) NOT NULL,
  `ProvinceArea` varchar(20) CHARACTER SET utf8 NOT NULL,
  `StudentClass` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Batch` varchar(50) CHARACTER SET utf8 NOT NULL,
  `ScoreLine` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3652 DEFAULT CHARSET=latin1;

/*Table structure for table `college_detail_ewt` */

DROP TABLE IF EXISTS `college_detail_ewt`;

CREATE TABLE `college_detail_ewt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolname` char(50) DEFAULT NULL,
  `f985` char(4) DEFAULT NULL,
  `f211` char(4) DEFAULT NULL,
  `fyan` char(4) DEFAULT NULL,
  `address` char(15) DEFAULT NULL,
  `levels` char(15) DEFAULT NULL,
  `attach_to` char(20) DEFAULT NULL,
  `school_rank` char(4) DEFAULT NULL,
  `schooltype` char(15) DEFAULT NULL,
  `character` char(15) DEFAULT NULL,
  `schoolid` char(10) DEFAULT NULL,
  `postal_address` text,
  `tel` text,
  `key_discipline` char(15) DEFAULT NULL COMMENT '重点学科',
  `faculty` char(50) DEFAULT NULL COMMENT '师资力量',
  `official_website` char(100) DEFAULT NULL,
  `school_img` char(100) DEFAULT '../static/school-img/江西师范大学.jpg',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2797 DEFAULT CHARSET=utf8;

/*Table structure for table `college_major` */

DROP TABLE IF EXISTS `college_major`;

CREATE TABLE `college_major` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolname` char(100) DEFAULT NULL,
  `edudirectly` char(15) DEFAULT NULL,
  `f985` char(4) DEFAULT NULL,
  `f211` char(4) DEFAULT NULL,
  `schoolprovince` char(30) DEFAULT NULL,
  `specialtype` char(30) DEFAULT NULL,
  `specialtyname` char(30) DEFAULT NULL,
  `level` char(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=146710 DEFAULT CHARSET=utf8;

/*Table structure for table `college_schoolscoreline` */

DROP TABLE IF EXISTS `college_schoolscoreline`;

CREATE TABLE `college_schoolscoreline` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name_School` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Area_School` varchar(20) CHARACTER SET utf8 NOT NULL,
  `DateYear` int(11) NOT NULL,
  `Area_Student` varchar(20) CHARACTER SET utf8 NOT NULL,
  `StudentClass` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Batch` varchar(50) CHARACTER SET utf8 NOT NULL,
  `MaxScore` int(11) NOT NULL,
  `MeanScore` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=536723 DEFAULT CHARSET=latin1;

/*Table structure for table `college_score` */


DROP TABLE IF EXISTS `college_scoreparm`;

CREATE TABLE `college_scoreparm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` varchar(20) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `years` varchar(10) DEFAULT NULL,
  `score` varchar(10) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43387 DEFAULT CHARSET=utf8;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ewt_new_jiangxi` */

DROP TABLE IF EXISTS `ewt_new_jiangxi`;

CREATE TABLE `ewt_new_jiangxi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolname` char(30) DEFAULT NULL,
  `profession` char(30) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `admission_number` int(11) DEFAULT NULL,
  `studenttype` char(10) DEFAULT NULL,
  `levels` char(10) DEFAULT NULL,
  `batch` char(10) DEFAULT NULL,
  `YEAR` int(11) DEFAULT NULL,
  `school_province` char(10) DEFAULT NULL,
  `province` char(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=412766 DEFAULT CHARSET=utf8;

/*Table structure for table `ewt_new_jx_mean` */

DROP TABLE IF EXISTS `ewt_new_jx_mean`;

CREATE TABLE `ewt_new_jx_mean` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` varchar(10) DEFAULT NULL,
  `schoolprovince` varchar(10) DEFAULT NULL,
  `schoolname` varchar(30) DEFAULT NULL,
  `profession` varchar(30) DEFAULT NULL,
  `studentType` varchar(4) DEFAULT NULL,
  `batch` varchar(10) DEFAULT NULL,
  `getnum` int(11) DEFAULT NULL,
  `meanscore` int(11) DEFAULT NULL,
  `meanrank` int(11) DEFAULT NULL,
  `diffscore` int(11) DEFAULT NULL,
  `schooltype` char(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29335 DEFAULT CHARSET=utf8;

/*Table structure for table `profession` */

DROP TABLE IF EXISTS `profession`;

CREATE TABLE `profession` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_type` varchar(10) CHARACTER SET utf8 NOT NULL,
  `subject_name` varchar(30) CHARACTER SET utf8 NOT NULL,
  `major_class` varchar(50) CHARACTER SET utf8 NOT NULL,
  `major_name` varchar(50) CHARACTER SET utf8 NOT NULL,
  `major_code` varchar(10) CHARACTER SET utf8 NOT NULL,
  `major_degree` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `major_time` varchar(30) CHARACTER SET utf8 NOT NULL,
  `major_course` varchar(400) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1304 DEFAULT CHARSET=latin1;

/*Table structure for table `profession_rank` */

DROP TABLE IF EXISTS `profession_rank`;

CREATE TABLE `profession_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `major_code` varchar(10) CHARACTER SET utf8 NOT NULL,
  `major_name` varchar(50) CHARACTER SET utf8 NOT NULL,
  `rank_num` int(11) NOT NULL,
  `rank_school` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6204 DEFAULT CHARSET=latin1;

/*Table structure for table `province_score` */

DROP TABLE IF EXISTS `province_score`;

CREATE TABLE `province_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `province` char(10) DEFAULT NULL,
  `year` char(6) DEFAULT NULL,
  `type` char(10) DEFAULT NULL,
  `bath` char(20) DEFAULT NULL,
  `score` char(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2832 DEFAULT CHARSET=utf8;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `stuprovince` varchar(10) NOT NULL,
  `stutype` varchar(2) NOT NULL,
  `schoolAddress` varchar(30) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
#修改表
UPDATE ewt_new_jx_mean a,
(SELECT schoolname,schooltype FROM college_detail_ewt ) b SET a.schooltype=b.schooltype WHERE a.schoolname=b.schoolname

#创建带有分差和地区批次线的表
CREATE TABLE ewt_new_jx4 (SELECT a.*,b.`score` AS 'province_score',a.score-b.score AS 'score_diff' FROM ewt_new_jx2 a LEFT JOIN province_score b ON a.year=b.year AND a.batch=b.batch AND a.studenttype=b.type AND a.province=b.province)
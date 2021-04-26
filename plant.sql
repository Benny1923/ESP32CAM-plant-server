-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2021 年 04 月 26 日 16:55
-- 伺服器版本： 5.7.33-0ubuntu0.18.04.1
-- PHP 版本： 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `plant`
--
CREATE DATABASE IF NOT EXISTS `plant` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `plant`;

-- --------------------------------------------------------

--
-- 資料表結構 `plant_automatic`
--

CREATE TABLE `plant_automatic` (
  `module` varchar(10) NOT NULL COMMENT '模組',
  `start` varchar(10) DEFAULT NULL COMMENT '起始時間',
  `end` varchar(10) DEFAULT NULL COMMENT '終止時間',
  `min` int(11) DEFAULT NULL COMMENT '啟動閥值',
  `max` int(11) DEFAULT NULL COMMENT '停止閥值',
  `cam_nightmode` tinyint(1) DEFAULT NULL,
  `cam_interval` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='自動操作';

--
-- 傾印資料表的資料 `plant_automatic`
--

INSERT INTO `plant_automatic` (`module`, `start`, `end`, `min`, `max`, `cam_nightmode`, `cam_interval`) VALUES
('camera', '08:09', '17:00', NULL, NULL, 0, 12),
('light', '12:02', '17:03', 22, 17, NULL, NULL),
('sprinklers', '06:01', '07:29', 27, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 資料表結構 `plant_gif`
--

CREATE TABLE `plant_gif` (
  `id` int(11) NOT NULL,
  `timestamp` date DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `plant_message`
--

CREATE TABLE `plant_message` (
  `id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `plant_photo`
--

CREATE TABLE `plant_photo` (
  `id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `plant_status`
--

CREATE TABLE `plant_status` (
  `id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL COMMENT '時間',
  `moisture` int(11) NOT NULL COMMENT '土壤濕度',
  `tankfluid` int(11) NOT NULL COMMENT '水箱水位',
  `lux` int(11) NOT NULL COMMENT '亮度'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='紀錄';

-- --------------------------------------------------------

--
-- 資料表結構 `plant_user`
--

CREATE TABLE `plant_user` (
  `id` int(11) NOT NULL,
  `account` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `plant_automatic`
--
ALTER TABLE `plant_automatic`
  ADD PRIMARY KEY (`module`) USING BTREE;

--
-- 資料表索引 `plant_gif`
--
ALTER TABLE `plant_gif`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`);

--
-- 資料表索引 `plant_message`
--
ALTER TABLE `plant_message`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`);

--
-- 資料表索引 `plant_photo`
--
ALTER TABLE `plant_photo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`);

--
-- 資料表索引 `plant_status`
--
ALTER TABLE `plant_status`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`);

--
-- 資料表索引 `plant_user`
--
ALTER TABLE `plant_user`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_gif`
--
ALTER TABLE `plant_gif`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_message`
--
ALTER TABLE `plant_message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_photo`
--
ALTER TABLE `plant_photo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_status`
--
ALTER TABLE `plant_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_user`
--
ALTER TABLE `plant_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

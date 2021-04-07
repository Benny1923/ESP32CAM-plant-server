-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2021-04-07 09:13:13
-- 伺服器版本： 10.4.17-MariaDB
-- PHP 版本： 8.0.2

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

-- --------------------------------------------------------

--
-- 資料表結構 `plant_automatic`
--

CREATE TABLE `plant_automatic` (
  `module` varchar(10) NOT NULL COMMENT '模組',
  `start` time DEFAULT NULL COMMENT '起始時間',
  `end` time DEFAULT NULL COMMENT '終止時間',
  `min` int(11) DEFAULT NULL COMMENT '啟動閥值',
  `max` int(11) DEFAULT NULL COMMENT '停止閥值',
  `automode` tinyint(1) NOT NULL COMMENT '操作開關',
  `spacing` varchar(255) DEFAULT NULL COMMENT '拍攝間隔'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='自動操作';

-- --------------------------------------------------------

--
-- 資料表結構 `plant_image`
--

CREATE TABLE `plant_image` (
  `timestamp` datetime NOT NULL COMMENT '時間',
  `filename` longblob NOT NULL COMMENT '檔案名稱'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='照片';

-- --------------------------------------------------------

--
-- 資料表結構 `plant_operation`
--

CREATE TABLE `plant_operation` (
  `module` varchar(10) NOT NULL COMMENT '模組',
  `ison` tinyint(1) NOT NULL COMMENT '啟動狀態',
  `isauto` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 資料表結構 `plant_status`
--

CREATE TABLE `plant_status` (
  `timestamp` datetime NOT NULL COMMENT '時間',
  `moisture` int(11) NOT NULL COMMENT '土壤濕度',
  `tankfluid` int(11) NOT NULL COMMENT '水箱水位',
  `ph` float NOT NULL COMMENT '酸鹼值',
  `online` tinyint(1) NOT NULL COMMENT '上線狀態'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='紀錄';

-- --------------------------------------------------------

--
-- 資料表結構 `plant_user`
--

CREATE TABLE `plant_user` (
  `id` int(11) NOT NULL,
  `account` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `plant_status`
--
ALTER TABLE `plant_status`
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
-- 使用資料表自動遞增(AUTO_INCREMENT) `plant_user`
--
ALTER TABLE `plant_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 09 Mar 2021, 15:37:30
-- Sunucu sürümü: 10.1.38-MariaDB
-- PHP Sürümü: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `apremen`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `customer_service`
--

CREATE TABLE `customer_service` (
  `cid` int(11) NOT NULL,
  `cName` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `pName` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `process` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Tablo döküm verisi `customer_service`
--

INSERT INTO `customer_service` (`cid`, `cName`, `pName`, `process`) VALUES
(1, 'CUSTOMER1', 'product_x', 'MACHINE-1 LOREM IPSUM DOLOR SIT AMET CONSECTETUR \nADIPISCING ELIT 1,MACHINE-4 VEL PLACERAT \nEX RHONCUS 2,MACHINE-2 CRAS DICTUM RISUS \nEU ORCI DIGNISSIM 3'),
(1, 'CUSTOMER1', 'product_y', 'MACHINE-1 IN AT FRINGILLA NUNC 1,MACHINE-3 UT SCELERISQUE LEO 2'),
(1, 'CUSTOMER1', 'product_z', 'MACHINE-3 ALIQUAM NEC \nHENDRERIT EST 1,MACHINE-1 CRAS A \nFACILISIS NEQUE 2,MACHINE-2 IN IN EFFICITUR ODIO 3');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `customer_service`
--
ALTER TABLE `customer_service`
  ADD PRIMARY KEY (`cid`,`pName`(100));
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

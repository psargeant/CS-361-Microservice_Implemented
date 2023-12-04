-- phpMyAdmin SQL Dump
-- version 5.2.1-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 03, 2023 at 01:15 AM
-- Server version: 10.6.15-MariaDB-log
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs361_bowlinst`
--

-- --------------------------------------------------------

--
-- Table structure for table `Dogs`
--

CREATE TABLE `Dogs` (
  `dogID` int(11) NOT NULL,
  `dogName` varchar(60) NOT NULL,
  `dogSize` varchar(60) NOT NULL,
  `dogAge` varchar(60) NOT NULL,
  `homeZip` varchar(15) NOT NULL,
  `playTimes` varchar(255) NOT NULL,
  `prefMethod` varchar(20) DEFAULT NULL,
  `prefInfo` varchar(60) DEFAULT NULL,
  `picOne` blob DEFAULT NULL,
  `picTwo` blob DEFAULT NULL,
  `picThree` blob DEFAULT NULL,
  `picFour` blob DEFAULT NULL,
  `picFive` blob DEFAULT NULL,
  `userID` int(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Dogs`
--

INSERT INTO `Dogs` (`dogID`, `dogName`, `dogSize`, `dogAge`, `homeZip`, `playTimes`, `prefMethod`, `prefInfo`, `picOne`, `picTwo`, `picThree`, `picFour`, `picFive`, `userID`) VALUES
(3, 'Ember', 'Small (6-20 lbs)', '1 - 3 years', '97370', 'Evening (5 - 10)', 'Email', 'tresaroseb@gmail.com', NULL, NULL, NULL, NULL, NULL, 13),
(4, 'Zelda Rose', 'Small (6-20 lbs)', '1 - 3 years', '97330', 'Evening (5 - 10)', 'Email', 'tim.b.harris@gmail.com', NULL, NULL, NULL, NULL, NULL, 13);

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `userID` int(60) NOT NULL,
  `firstName` varchar(60) NOT NULL,
  `lastName` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `passwordHash` varchar(255) NOT NULL,
  `profilePic` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`userID`, `firstName`, `lastName`, `email`, `passwordHash`, `profilePic`) VALUES
(13, 'Tresa', 'Bowlin', 'tresaroseb@gmail.com', 'Brb020152!', NULL),
(14, 'Tim', 'Harris', 'tim.b.harris@gmail.com', 'Zelda2022!', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Dogs`
--
ALTER TABLE `Dogs`
  ADD PRIMARY KEY (`dogID`),
  ADD KEY `Dogs_ibfk_1` (`userID`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Dogs`
--
ALTER TABLE `Dogs`
  MODIFY `dogID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `userID` int(60) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Dogs`
--
ALTER TABLE `Dogs`
  ADD CONSTRAINT `Dogs_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `Users` (`userID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

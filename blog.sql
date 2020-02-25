-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2020 at 07:00 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(15, 'tripti ', '9058866481', 'BC ignore karta h', '2020-02-22 13:28:52', 'tripti@email.com'),
(16, 'kuvh', '9358616890', 'hello', '2020-02-25 07:53:33', 'abcd123@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(50) NOT NULL,
  `tittle` varchar(50) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `sub_tittle` text NOT NULL,
  `img_file` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `tittle`, `slug`, `content`, `sub_tittle`, `img_file`, `date`) VALUES
(1, 'WHY SO SERIOUS !!!!!!', 'first-post', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio, adipisci quas excepturi maxime quae totam ducimus consectetur?\r\n\r\nLorem ipsum dolor sit amet, consectetur adipisicing elit. Eius praesentium recusandae illo eaque architecto error, repellendus iusto reprehenderit, doloribus, minus sunt. Numquam at quae voluptatum in officia voluptas voluptatibus, minus!\r\n\r\nLorem ipsum dolor sit amet, consectetur adipisicing elit. ex itaque esse est vero natus quae optio aperiam soluta voluptatibus corporis atque iste neque sit tempora!', 'This is about joker???????', 'poster.png', '2020-02-25 22:51:22'),
(3, 'Lets Smile!', 'lets+smile', 'lets put a smile on that face.\r\nA very famous quote about joker.', 'ha bhai sub tittle ', 'about-bg.jpg', '2020-02-16 14:12:33'),
(26, 'fresh????', 'mu', 'ffff', 'ankit', 'design.png', '2020-02-20 18:08:45'),
(27, 'new blog', 'd', 'nn', 'abs', 'ieslogo.png', '2020-02-20 18:09:05'),
(28, 'ye he Uttu', 'i-l-t', 'kya kru pat hi nahi rahi', 'i l t', 'design.png', '2020-02-22 13:31:53'),
(29, 'new-posttttt', 'n-p', 'have fun', 'ok', '3300250.jpg', '2020-02-25 07:56:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

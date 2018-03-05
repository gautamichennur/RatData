CREATE TABLE `ratchatdb`.`ratsite` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `time` DATETIME NOT NULL , 
    `is_outside` BOOLEAN NOT NULL , 
    `is_alive` BOOLEAN NOT NULL , 
    `location` VARCHAR(255) NOT NULL , 
    PRIMARY KEY (`id`)) 
ENGINE = InnoDB;
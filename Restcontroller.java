package com.example.Angularjs.demo;

import java.io.IOException;

import javax.mail.MessagingException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Restcontroller {
	
	@Autowired
	Sendmail service;
	
	
	@GetMapping("/mail")
	public String sendmail()
	{
		service.sendmail();
		return "send mail successfully";
	}
	
	@GetMapping("/image")
	public String Insert()
	{
		return service.Insert();
	}
	
	
	

}

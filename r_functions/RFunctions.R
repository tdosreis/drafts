'%!in%' <- function(x,y)!('%in%'(x,y))

ToCharacter <- function(df, vars){
    for (i in vars){
        df[,i] <- as.character(df[,i])
    }
    return(df)
}

ToNumeric <- function(df,vars){
    for (i in vars){
        df[,i] <- as.numeric(as.character(df[,i]))
    }
    return(df)
}   

InsertMeanCol <- function(df,vars){
    for (i in vars){
        df[,paste('mean',i,sep='_')] <- mean(df[,i]) 
    }    
    return(df)
}

InsertMedian <- function(df,vars){
    for(i in vars){
        ifelse(is.na(df[,i]) !=0,df[is.na(df[,i]), i] <- median(df[,i], na.rm = TRUE),NA)
    }
    return(df)
}

InsertMean <- function(df,vars){
    for(i in vars){
        ifelse(is.na(df[,i]) !=0,df[is.na(df[,i]), i] <- mean(df[,i], na.rm = TRUE),NA)
    }
    return(df)
}

LabelEncoder <- function(df, vars){
    for(i in vars){
        df[,i] <- match(df[,i], unique(df[,i]))
  }
  return(df)
}

IsGranular <- function(df,vars,thresh=0.2){
    granular <- c()
    for(i in vars){
        QuantUniVals <- length(unique(df[,i]))
        QuantEntries <- length(df[,i])
        ifelse(QuantUniVals/QuantEntries >= thresh, granular <- append(granular, i), NA)    
    }
    return(granular)
} 

DisplayStats <- function(df){
    IndexVals <- c()
    for (i in names(df)){    
        IndexVals <- append(IndexVals, which(names(df)==i))
    }

    QuantUni  <- sapply(df, function(x) length(unique(x)))
    QuantNaN  <- sapply(df, function(x) sum(is.na(x)))
    ClassType <- sapply(df, function(x) class(x))
    QuantTot  <- sapply(df, function(x) length(is.na(x)))
    PctNaN    <- round(QuantNaN/QuantTot,digits = 2)

    all_df <- cbind(IndexVals, QuantNaN, QuantTot, QuantUni, ClassType, PctNaN)
    all_df <- setnames(setDT(as.data.frame(all_df), keep.rownames = TRUE)[],1,'Variable')

    NotFactors <- names(ClassType[ClassType != 'factor'])

    MeanVals   <- sapply(df[,NotFactors], function(x) round(mean(as.numeric(x),   na.rm=T), digits = 2))
    MedianVals <- sapply(df[,NotFactors], function(x) round(median(as.numeric(x), na.rm=T), digits = 2))
    MaxVals    <- sapply(df[,NotFactors], function(x) round(max(as.numeric(x),    na.rm=T), digits = 2))
    MinVals    <- sapply(df[,NotFactors], function(x) round(min(as.numeric(x),    na.rm=T), digits = 2))
    SumVals    <- sapply(df[,NotFactors], function(x) round(sum(as.numeric(x),    na.rm=T), digits = 2))
    VarVals    <- sapply(df[,NotFactors], function(x) round(var(as.numeric(x),    na.rm=T), digits = 2))

    numeric_df <- cbind(MeanVals, MedianVals, MaxVals, MinVals, SumVals, VarVals)                     
    numeric_df <- setnames(setDT(as.data.frame(numeric_df), keep.rownames = TRUE)[],1,'Variable')

    NLevels   <- sapply(df[,-which(names(df) %in% NotFactors)], function(x) length(levels(factor(x))))   
    factor_df <- setnames(setDT(as.data.frame(NLevels), keep.rownames = TRUE)[],1,'Variable')

    stats_df <- merge(all_df  ,  factor_df, by="Variable", all = T)
    stats_df <- merge(stats_df, numeric_df, by='Variable', all = T)

    return(stats_df)      
}

RandomSample <- function(df,TestSize=.3,RandomState=101){
    RandomState <- set.seed(RandomState)
    df_sample <- df[sample(1:nrow(df), TestSize*nrow(df)),]
    return(df_sample)
}

TrainTestSplit <- function(df,y,TestSize=.3,RandomState=101){
    
    y_index <- which(names(df) == y)
    
    X_test <- RandomSample(df,TestSize,RandomState) 
    y_test <- X_test[, y_index]
    X_test <- X_test[,-y_index]
    
    X_test_index <- as.numeric(as.character(rownames(X_test)))
    
    X_train <- df[-X_test_index,]
    y_train <- X_train[, y_index]
    X_train <- X_train[,-y_index]
    
    dfs <- list(X_train,X_test,y_train,y_test)
    
    return(dfs)
}

GetVarIndex <- function(df){
    index <- variable <- c()
    for(i in 1:ncol(df)){
        index    <- append(index,i)
        variable <- append(variable,names(df)[i])
    }
    df_ix <- (cbind(variable,index))
    return(df_ix)
}

ReplaceOutlier <- function(df, Quant1=.25, Quant3=.75){
    
    quantiles <- quantile(df,c(Quant1,Quant3))
    
    q1 <- as.numeric(as.character(quantiles[1]))
    q3 <- as.numeric(as.character(quantiles[2]))
    
    IQR <- q3 - q1
    
    Q1 <- q1 - (IQR*1.5)
    Q3 <- q3 + (IQR*1.5)
    
    df[ df < Q1 ] <- Q1
    df[ df > Q3 ] <- Q3
    
    return(df)
}
    
ReplaceOutliers <- function(df, vars){
    for(i in vars){
        df[,i] <- ReplaceOutlier(df[,i])
    }
    return(df)
}

TrainTestSplitXGB <- function(df, vars, targets, TestSize = .3, RandomState = 101){
    df_xgb   <- df[,vars]
    df_test  <- RandomSample(df_xgb, TestSize = TestSize, RandomState = RandomState)
    df_train <- df_xgb[-as.numeric(as.character(rownames(df_test))), ]
    y_test   <- df_test[,target]
    y_train  <- df_train[,target]
    dfs      <- list(df_train, df_test, y_train, y_test)
    return(dfs)
}

MakeDummies <- function(v, prefix = '') {
  s <- sort(unique(v))
  d <- outer(v, s, function(v, s) 1L * (v == s))
  colnames(d) <- paste0(prefix, s)
  d
}
             
#########################
### Information Value ###
#########################
SplitDataFrame <- function(df,target,RandomState=101){
    Ones  <- df[which(df[,target] == 1), ]  # all 1's
    Zeros <- df[which(df[,target] == 0), ]  # all 0's

    set.seed(RandomState)
    RowsOnes  <- sample(1:nrow(Ones), 0.7*nrow(Ones))
    RowsZeros <- sample(1:nrow(Zeros),0.7*nrow(Zeros))

    TrainingOnes  <- Ones[RowsOnes, ]  
    TrainingZeros <- Zeros[RowsZeros, ]
    TrainingData  <- rbind(TrainingOnes, TrainingZeros)
    
    return(TrainingData)   
}   
             
InfoValDF <- function(FactorVars, ContinuousVars){
    
    VARS <- c(FactorVars, ContinuousVars)
    IV <- numeric(length(FactorVars) + length(ContinuousVars))
    
    iv_ <- data.frame(VARS, IV)
    
    return(iv_)
}
             
InfoValue <- function(trainingData,factor_vars,continuous_vars,y){
    
    iv_<- iv_df(factor_vars,continuous_vars)
    
    for(i in factor_vars){
      smb <- smbinning.factor(trainingData, y, i)  # WOE table
      if(class(smb) != "character"){ # heck if some error occured
        iv_[iv_$VARS == i, "IV"] <- smb$iv
      }
    }

    for(i in continuous_vars){
      smb <- smbinning(trainingData, y, i)  # WOE table
      if(class(smb) != "character"){  # any error while calculating scores.
        iv_[iv_$VARS == i, "IV"] <- smb$iv
      }
    }
    
    iv_ <- iv_[order(-iv_$IV),]
    
    return(iv_) 
}      
             
MultiPlot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)

  plots <- c(list(...), plotlist)

  numPlots = length(plots)

  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                    ncol = cols, nrow = ceiling(numPlots/cols))
  }

 if (numPlots==1) {
    print(plots[[1]])

  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))

    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))

      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}
             
vifStepwise <- function(df,contents){
    
    vars.del <- c() # lista de variaveis removidas

    stop <- 0

    df_tmp <- df[,contents]

    print('teste de multicolinearidade ...')

    while (stop < 1){

        vif.vals <- c()

        fit1 <- glm(default.payment.next.month ~ . , data=df_tmp, family=binomial(link="logit"))

        vif.vars <- vif(fit1)

        for(i in vif.vars){
            vif.vals <- append(vif.vals, i)
            }

        vif_df <- as.data.frame(cbind(names(vif.vars),vif.vals))

        vif_df[,'vif.vals'] <- as.numeric(as.character(vif_df[,'vif.vals']))

        vif_df <- vif_df[order(vif_df$vif.vals,decreasing = T),]

        var.val <- as.numeric(as.character(vif_df[1,2]))

        var.del <- as.character(vif_df[1,1])

        if(var.val >= 5){

            cat('\n variavel: ', var.del, ' ===>>> VIF : ', var.val)

            vars.del <- append(vars.del, var.del)

            cat('\n dim - antes', dim(df_tmp))

            df_tmp[,var.del] <- NULL

            cat('\n dim - depois', dim(df_tmp),'\n')

        }else{
            stop <- 1
        }

    }
    cat('\n variaveis a deletar (criterio VIF stepwise) ===>>> \n', vars.del)
  
 return(vars.del)
    
}
             
ggplotConfusionMatrix <- function(m){
  library(scales)
  mytitle <- paste("Acuracia = ", percent_format()(m$overall[1]),"Kappa", percent_format()(m$overall[2]))
  
  p <- ggplot(data = as.data.frame(m$table), aes(x = Reference, y = Prediction)) +
    geom_tile(aes(fill = log(Freq)), colour = "white") +
    scale_fill_gradient(low = "white", high = "steelblue") +
    geom_text(aes(x = Reference, y = Prediction, label = Freq)) +
    theme(legend.position = "none") +
    ggtitle(mytitle)
  return(p)
}            